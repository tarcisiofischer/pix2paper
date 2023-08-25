from typing import *
from PIL import Image
import argparse


def generate_pixel_table_from(image_filename: str):
    '''
    :param image_filename:
        The pixel art image file to be converted
    :return:
        A table with numbers representing each color in the pixel art file
    '''
    im = Image.open(image_filename)
    colormap = {}
    pixel_table = []
    for i in range(im.width):
        pixel_table.append([])
        for j in range(im.height):
            px = im.getpixel((j, i))
            px = px[:3]
            if px not in colormap:
                colormap[px] = len(colormap)
            cid = colormap[px]
            pixel_table[-1].append(cid)
    return pixel_table


def generate_html_contents_from(pixel_table: List[List[int]]):
    '''
    :param pixel_table:
        Pixel art table (..see: generate_pixel_table_from)
    :return:
        Contents representing the table using HTML format
    '''
    css_data = ''
    css_data += 'table { border: 0px; padding: 0px; margin: 0px; border-collapse: collapse; border-spacing: 0; }'
    css_data += 'tbody { border: 0px; padding: 0px; margin: 0px; }'
    css_data += 'tr { border: 0px; padding: 0px; margin: 0px; }'
    css_data += 'td { border: 1px solid black; padding: 0px; margin: 0px; width: 20px; height: 20px; text-align: center; color: gray; }'

    html_data = ''
    html_data += '<style>'
    html_data += css_data
    html_data += '</style>'
    html_data += '<table>'
    for row in pixel_table:
        html_data += '<tr>'
        for col in row:
            html_data += f'<td>{col}</td>'
        html_data += '</tr>'
    html_data += '</table>'
    return html_data


def main():
    parser = argparse.ArgumentParser("pix2paper")
    parser.add_argument("-i", "--input", required=True, help="The input pixel art image file", type=str)
    parser.add_argument("-o", "--output", required=False, help="The output html file name", type=str, default="output.html")
    args = parser.parse_args()

    pixel_table = generate_pixel_table_from(args.input)
    with open(args.output, 'w') as out:
        out.write(generate_html_contents_from(pixel_table))


if __name__ == "__main__":
    main()
