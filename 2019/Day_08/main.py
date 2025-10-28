"""
--- Day 8: Space Image Format ---

The Elves' spirits are lifted when they realize you have an opportunity to
reboot one of their Mars rovers, and so they are curious if you would spend a
brief sojourn on Mars. You land your ship near the rover.

When you reach the rover, you discover that it's already in the process of
rebooting! It's just waiting for someone to enter a BIOS password. The Elf
responsible for the rover takes a picture of the password (your puzzle input)
and sends it to you via the Digital Sending Network.

Unfortunately, images sent via the Digital Sending Network aren't encoded with
any normal encoding; instead, they're encoded in a special Space Image Format.
None of the Elves seem to remember why this is the case. They send you the
instructions to decode it.

Images are sent as a series of digits that each represent the color of a single
pixel. The digits fill each row of the image left-to-right, then move downward
to the next row, filling rows top-to-bottom until every pixel of the image is
filled.

Each image actually consists of a series of identically-sized layers that are
filled in this way. So, the first digit corresponds to the top-left pixel of the
first layer, the second digit corresponds to the pixel to the right of that on
the same layer, and so on until the last digit, which corresponds to the
bottom-right pixel of the last layer.

For example, given an image 3 pixels wide and 2 pixels tall, the image data
123456789012 corresponds to the following image layers:

    Layer 1: 123
             456

    Layer 2: 789
             012

The image you received is 25 pixels wide and 6 pixels tall.

PART 1: To make sure the image wasn't corrupted during transmission, the Elves
        would like you to find the layer that contains the fewest 0 digits. On
        that layer, what is the number of 1 digits multiplied by the number of 2
        digits?

Now you're ready to decode the image. The image is rendered by stacking the
layers and aligning the pixels with the same positions in each layer. The digits
indicate the color of the corresponding pixel: 0 is black, 1 is white, and 2 is
transparent.

The layers are rendered with the first layer in front and the last layer in
back. So, if a given position has a transparent pixel in the first and second
layers, a black pixel in the third layer, and a white pixel in the fourth layer,
the final image would have a black pixel at that position.

For example, given an image 2 pixels wide and 2 pixels tall, the image data
0222112222120000 corresponds to the following image layers:

    Layer 1: 02
             22

    Layer 2: 11
             22

    Layer 3: 22
             12

    Layer 4: 00
             00

Then, the full image can be found by determining the top visible pixel in each
position:



        -   The top-left pixel is black because the top layer is 0.

        -   The top-right pixel is white because the top layer is 2
            (transparent), but the second layer is 1.

        -   The bottom-left pixel is white because the top two layers are 2, but
            the third layer is 1.

        -   The bottom-right pixel is black because the only visible pixel in
            that position is 0 (from layer 4).

So, the final image looks like this:

    01
    10

PART 2: What message is produced after decoding your image?
"""


class DSNImage:
    def __init__(self, raw_data_file: str, img_dims: (int, int)):
        self.dims = img_dims
        self.pixels = []

        with open(raw_data_file, "r") as fp:
            raw_data = fp.read().strip()

            # Fill the image layer by layer
            for layer_idx in range(len(raw_data) // (self.dims[0] * self.dims[1])):
                self.pixels.append(
                    [
                        int(x)
                        for x in raw_data[
                            layer_idx
                            * self.dims[0]
                            * self.dims[1] : (layer_idx + 1)
                            * self.dims[0]
                            * self.dims[1]
                        ]
                    ]
                )

    def checksum(self) -> int:
        """
        Find the layer that contains the fewest 0 digits. Ont that layer return
        the number of 1 digits multiplied by the number of 2 digits.
        """
        min_zeros = self.dims[0] * self.dims[1]
        min_zero_layer = None

        # Find the layer with the fewest zeros
        for layer_idx in range(len(self.pixels)):
            layer_zero_cnt = self.pixels[layer_idx].count(0)

            if layer_zero_cnt < min_zeros:
                min_zeros = layer_zero_cnt
                min_zero_layer = layer_idx

        # Calculate the checksum
        num_1s = self.pixels[min_zero_layer].count(1)
        num_2s = self.pixels[min_zero_layer].count(2)

        return num_1s * num_2s

    def __str__(self):
        """
        Render image, based on the colour values:

            0 = black,
            1 = white
            2 = transparent

        The layers are rendered with the first layer in front and the last layer
        in back.
        """
        render = ""

        # Build the image pixel by pixel
        for col_idx in range(self.dims[1]):
            for row_idx in range(self.dims[0]):

                # Dig deeper till either a black or white pixel is found
                for layer_idx in range(len(self.pixels)):
                    curr_pxl = self.pixels[layer_idx][row_idx + col_idx * self.dims[0]]

                    if curr_pxl == 0:
                        render += " "
                        break

                    elif curr_pxl == 1:
                        render += "█"
                        break

                else:
                    raise Exception(f"No colour found in ({row_idx}{col_idx})")

            render += "\n"
        return render


if __name__ == "__main__":
    bios_secret = DSNImage("./data/input_0.txt", (25, 6))
    print(f"Part 1 = {bios_secret.checksum()}\nPart 2 =\n{bios_secret}")
