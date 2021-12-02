# ImageMagick
ImageMagick can be used to manipulate images.

## Usage
- magick input [options] output
- convert input [options] output

ImageMagick can convert between file formats by having the extension of the
output differ from the input.

## Options
- **-resize [percentage]%, -resize[width]x[height]** resize an image
    - By default, resize keeps the aspect ratio and scales the larger dimension to fit inside the specified area defined by width times height.
    - ^ can be placed after the height dimension to indicate resizing the smaller dimension instead.
    - \\\! can be placed after the height dimension to ignore the aspect ratio.
- **-rotate [degrees]** rotate an image, positive is clockwise and negative is counter-clockwise
- **-crop [width]x[height]+[x]+[y]** crop an image to width times height, starting at the coordinate (x, y).
- **-blur [radius]** blur an image
- **-sharpen [radius]** enhance/sharpen an image
- **-grayscale** grayscale an image
- **-gravity [type]** specify where to add text or subimages
- **-draw "[primitive(s)] [arguments]"** add objects, including text, to an image
- **-fuzz** remove edges that are nearly the same color as the corners
- **-trim** remove edges that are exactly the same color as the corners

## Tips
ImageMagick can also do inline image resizes and crops, where files are operated
on as they are read instead of finishing one image before moving on to the next.

- **magick '\*.jpg[64x64]' output** resize to 64x64
- **magick '\*.jpg[62x62+2+2]' output** crop to 62x62 starting from (2, 2)

*Page added on 2021-12-02*

