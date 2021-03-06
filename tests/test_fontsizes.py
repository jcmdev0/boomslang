#!/usr/bin/env python

from boomslang import Line, Plot
from ImageComparisonTestCase import ImageComparisonTestCase
import unittest

class FontSizesTest(ImageComparisonTestCase, unittest.TestCase):
    def __init__(self, testCaseName):
        super(FontSizesTest, self).__init__(testCaseName)
        self.imageName = "fontsizes.png"

    def constructImage(self):
        plot = Plot()

        line = Line()
        line.yValues = [25, 40, 30, 23, 10, 50]
        line.xValues = range(len(line.yValues))

        plot.add(line)
        plot.setXLabel("X Label")
        plot.setYLabel("Y Label")
        plot.setYLimits(0, 60)

        plot.setXTickLabelSize(24)
        plot.setYTickLabelSize(36)
        plot.setAxesLabelSize(18)

        plot.setPlotParameters(bottom=0.14)

        plot.save(self.imageName)

ImageComparisonTestCase.register(FontSizesTest)

if __name__ == "__main__":
    test = FontSizesTest("testImageComparison")

    test.constructImage()
