from falcor import *


def render_graph_DefaultRenderGraph():
    g = RenderGraph('DefaultRenderGraph')

    BSDFViewer = createPass("BSDFViewer", {'materialID': 0})
    g.addPass(BSDFViewer, "BSDFViewer")
    AccumulatePass = createPass("AccumulatePass", {'enabled': True, 'precisionMode': AccumulatePrecision.Double})
    g.addPass(AccumulatePass, "AccumulatePass")
    g.addEdge("BSDFViewer.output", "AccumulatePass.input")
    g.markOutput("AccumulatePass.output")

    return g


DefaultRenderGraph = render_graph_DefaultRenderGraph()
try:
    m.addGraph(DefaultRenderGraph)
except NameError:
    None
