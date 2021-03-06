from Location import Location
import warnings
from Utils import _check_min_matplotlib_version

class Legend(object):
    location = Location("location")

    def __init__(self, columns = 1, scatterPoints = 3, drawFrame = True,
                 location = "best", figLegend = False, labelSize = None,
                 bboxToAnchor = None):
        self.location = location
        self.labelSize = labelSize
        self.columns = columns
        self.scatterPoints = scatterPoints
        self.drawFrame = drawFrame
        self.figLegend = figLegend
        self.bboxToAnchor = bboxToAnchor

    def _genLegendKeywords(self, axes, handles, labels):
        legendKeywords = {}

        if self.columns > 1:
            if not _check_min_matplotlib_version(0, 98, 0):
                warnings.warn("Number of columns support not available "
                              "in versions of matplotlib prior to 0.98")
            else:
                legendKeywords["ncol"] = self.columns
                legendKeywords["scatterpoints"] = self.scatterPoints

        if self.labelSize is not None:
            legendKeywords["prop"] = {"size" : self.labelSize}

        if self.bboxToAnchor is not None:
            legendKeywords["bbox_to_anchor"] = bbox_to_anchor

        return legendKeywords

    def draw(self, figure, axes, handles, labels):
        legendKeywords = self._genLegendKeywords(axes, handles, labels)

        legend = None

        if self.figLegend:
            legend = fig.legend(handles, labels, loc=self.location,
                                **legendKeywords)
        else:
            legend = axes.legend(handles, labels, loc=self.location,
                                 **legendKeywords)

        if legend is not None:
            legend.draw_frame(self.drawFrame)
