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


if __name__ == "__main__":
    print(f"Part 1 = {DSNImage('./data/input_0.txt', (25, 6)).checksum()}")
