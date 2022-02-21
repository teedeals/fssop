# -*- coding: utf-8 -*-
"""
Spyder Editor
"""


#1 Tabs
#2 Tab first - sidebar dates, regions, Main page top region perf, Main bottom left insights, main bottom right pnl
#3 Tab second - sidebar, Main page top, Main bottom left, main bottom right
#4 page per region 


import streamlit as st
import pandas as pd
import plotly.express as px

# FS Codes
import numpy as np
import plotly
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
#import cufflinks as cf

su, ch, tr, roa, dc, fte, hc, ob, pl,dt, dt2, drs, ra, mt = None, None, None, None, None, None, None, None, None, None, None, None, None, None
with pd.ExcelFile("./GFA.xls") as reader:
    su = pd.read_excel(reader, sheet_name='Summary')
    ch = pd.read_excel(reader, sheet_name='ch')
    tr = pd.read_excel(reader, sheet_name='TR')
    roa = pd.read_excel(reader, sheet_name='ROA')
    dc = pd.read_excel(reader, sheet_name='DC')
    fte = pd.read_excel(reader, sheet_name='Employees')
    hc = pd.read_excel(reader, sheet_name='HC')
    ob = pd.read_excel(reader, sheet_name='Orderbook')
    pl = pd.read_excel(reader, sheet_name='P&L')
    dt = pd.read_excel(reader, sheet_name='dt')
    dt2 = pd.read_excel(reader, sheet_name='dt2')
    mt = pd.read_excel(reader, sheet_name='mt')
    ra = pd.read_excel(reader, sheet_name='RA')
    drs = pd.read_excel(reader, sheet_name='DRS')

suf = px.scatter(su, x="Direct Costs", y="Return on Asset",
                 size="Total Revenue", color="Region", hover_name="Region", size_max=80)
#suf.show()

#SHARE OF TOTAL RADIAL
figST = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = 22.5,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Region Performance: NA", 'font': {'size': 24}},
    delta = {'reference': 15, 'increasing': {'color': "Green"}},
    gauge = {
        'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkgreen"},
        'bar': {'color': "black"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 20], 'color': 'red'},
            {'range': [21, 35], 'color': 'orange'},
            {'range': [36, 100], 'color': 'green'}],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 0.75,
            'value': 22.5}}))

figST.update_layout(paper_bgcolor = "white", font = {'color': "black", 'family': "Arial"})

#figST.show()

#SHARE OF TOTAL RADIAL
figST2 = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = 32.8,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Region Performance: India", 'font': {'size': 24}},
    delta = {'reference': 15, 'increasing': {'color': "Green"}},
    gauge = {
        'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkgreen"},
        'bar': {'color': "black"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 20], 'color': 'red'},
            {'range': [21, 35], 'color': 'orange'},
            {'range': [36, 100], 'color': 'green'}],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 0.75,
            'value': 32.8}}))

figST2.update_layout(paper_bgcolor = "white", font = {'color': "black", 'family': "Arial"})

#figST2.show()

#SHARE OF TOTAL RADIAL
figST4 = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = 10.5,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Region Performance: North Central Europe", 'font': {'size': 24}},
    delta = {'reference': 15, 'increasing': {'color': "Green"}},
    gauge = {
        'axis': {'range': [None, 100], 'tickwidth': 1, 'tickcolor': "darkgreen"},
        'bar': {'color': "black"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 20], 'color': 'red'},
            {'range': [21, 35], 'color': 'orange'},
            {'range': [36, 100], 'color': 'green'}],
        'threshold': {
            'line': {'color': "black", 'width': 4},
            'thickness': 0.75,
            'value': 10.5}}))

figST4.update_layout(paper_bgcolor = "white", font = {'color': "black", 'family': "Arial"})

#figST4.show()

figTR = px.bar(tr, x='Region', y='Total Revenue', color='Cost Effectiveness')
#figTR.show()
#cost effectiveness
#figTRh = figTR.write_html('G_COSTREG.html')

drs2 =px.line(drs, y="Own Revenue", x="Period", color="Region", 
              title="Diminishing Returns (Revenues)")
#drs2.show()
#drsf2 = drs2.write_html('drs2.html')

#Chloropleth - need countries data
chf = px.choropleth(ch, locations="Country",
                    locationmode = "country names",
                    color="Return on Asset", 
                    hover_name="Country", 
                    #color_continuous_scale=px.colors.sequential.Plasma
                   )
#chf.show()
#chf1 = chf.write_html('GROA.html')
chf = px.choropleth(ch, locations="Country",
                    locationmode = "country names",
                    color="Return on Asset", 
                    hover_name="Country", 
                    #color_continuous_scale=px.colors.sequential.Plasma
                   )
#chf.show()
#chf1 = chf.write_html('GARVE.html')

#HC

categories = ['FRESH JOINERS','LATERAL JOINERS','MANAGED LEAVERS',
              'VOLUNTARY LEAVERS', 'HC NET ADDITION']

figh = go.Figure()

figh.add_trace(go.Scatterpolar(
      r=[340,822,98,158,877],
      theta=categories,
      fill='toself',
      name='FS I&D Global'
))

figh.add_trace(go.Scatterpolar(
      r=[483,474,423,340,496],
      theta=categories,
      fill='toself',
      name='North America'
))

figh.add_trace(go.Scatterpolar(
      r=[618,715,133,715,570],
      theta=categories,
      fill='toself',
      name='India'
))

figh.update_layout(
  polar=dict(
    radialaxis=dict(
      visible=True,
      range=[10, 1000]
    )),
  showlegend=True
)

#figh.show()

#Orderbook
figOB = px.sunburst(ob, path=['Year', 'Month', 'Site','Type'], values='Percent', color='Month')
#figOB.show()
#figob1 = figOB.write_html('GOB.html')

figp = go.Figure(go.Waterfall(
    name = "2018", orientation = "h", measure = ["relative", "relative", "total", "relative", "total", "relative",
                                              "relative", "relative", "relative", "relative", "total"],
    y = ["Revenue Own", "Revenue Purchased", "Revenue Total", "Direct Cost", "CM", "Gross", "Recovery",
       "IDC", "BDC", "SFC", "NR"],
    x = [130, 7, None, -120, None, -24, 33, -4,-2,-5, None],
    connector = {"mode":"between", "line":{"width":2, "color":"rgb(0, 0, 0)", "dash":"solid"}}
))

figp.update_layout(title = "Net Recovery Path 2020")

#figp.show()

#SANKEY P&L
color_link = ['lavender', 'lemonchiffon', 'lightblue', 'lightcoral', 'lightcyan', 'lightgreen', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue','lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'mediumaquamarine', 'palegreen', 'paleturquoise', 'palevioletred', 'beige']
fig18 = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
#      line = dict(color = "black", width = 0.5),
      label = ["Interest Income", "Income from Investments", "Interest on Inter-Bank funds", "Other Income", 
               "Total Income", 
               "Interest Expended", "Employee Cost", "One Time Liability", "ESOP Provisions", 
               "Total Costs", 
               "Profit before DT",
               "Depreciation", 
               "Income Tax", 
               "Net Profit"],
      color = ['rgba(31, 119, 180, 0.8)',
               'rgba(255, 127, 14, 0.8)',
               'rgba(44, 160, 44, 0.8)',
               'rgba(214, 39, 40, 0.8)',
               'rgba(148, 103, 189, 0.8)',
               'rgba(140, 86, 75, 0.8)',
               'rgba(227, 119, 194, 0.8)',
               'rgba(127, 127, 127, 0.8)',
               'rgba(188, 189, 34, 0.8)',
               'rgba(23, 190, 207, 0.8)',
               'rgba(31, 119, 180, 0.8)',
               'rgba(44, 160, 44, 0.8)',
               'rgba(214, 39, 40, 0.8)',
               'rgba(148, 103, 189, 0.8)'],
    ),
    link = dict(
      source = [0,1,2,3,
                4,
                5,6,7,8,
                9,
                10,
                11,
                12,
                13], 
      target = [4,4,4,4,10,9,9,9,9,10,13,13,13,None],
      value = [570, 113, 43, 19, 745, 188, 171, 12, 34, 305, 265, 8, 11, 246],
      color = color_link))])

fig18.update_layout(title_text= "P&L Path", font_size=15)
#fig18.show()

figdt = go.Figure()

region = ['North America', 'India', 'North Central Europe', 'South Central Europe']

for reg in region:
    figdt.add_trace(go.Violin(x=dt['Region'][dt['Region'] == reg],
                            y=dt['Revenue Own'][dt['Region'] == reg],
                            box_visible=True,
                            name=reg,
                            meanline_visible=True))
    
figdt.update_layout(title= "Business Stability", font_size=15)
#figdt.show()

figdt2 = go.Figure()

heads = ['Own Revenue','Purchase Revenue','Resource Costs', 'Support and BD']

for head in heads:
    figdt2.add_trace(go.Violin(x=dt2['Heads'][dt2['Heads'] == head],
                            y=dt2['Amount'][dt2['Heads'] == head],
                            box_visible=True,
                            name=head,
                            meanline_visible=True))
    
figdt.update_layout(title= "Business Stability", font_size=15)
#figdt2.show()

gmt = px.scatter_3d(mt, x = 'BU1',
                    y = 'BU2',
                    z = 'BU3',
                    color = 'Unnamed: 0')


#Streamlit app

import streamlit as st
import pandas as pd
import plotly.express as px

import numpy as np
import plotly
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go

#Streamlit app

#1 Load data - view data - use expander to show sample
#2 link to selects in sidebar
#3 link choice to charts on mainpage

st.sidebar.markdown("Inputs")

st.sidebar.file_uploader(' ')

st.title('Financial Performance Dashboards')


#Variables sidebar
start = st.sidebar.date_input('Start',value = pd.to_datetime('2021-01-01'))
end = st.sidebar.date_input('End',value = pd.to_datetime('2022-01-01'))

regions = ('All','APAC', 'FS Global', 'India', 'North CE', 'North America', 'South CE')
atype = ('Trends', 'Relationships', 'Composition', 'Comparison')
#perfd = ('Revenues', 'Attrition','Stability & Risk', 'Profitability','P&L Path', 'Ratios','Costs', 'People', 'Regional Performance', 'Ratio Analysis', 'Return on Assets', 'Orderbook')

trends = ('Revenues', 'Direct Cost','Attrition',  'People' )
rela = ('Attrition','Stability & Risk', 'Profitability', 'Ratio Analysis')
comt = ('P&L Path','Orderbook', 'Costs', 'Attrition' )
compa = ('Regional Performance', 'Return on Assets', 'Orderbook', 'People' )

dropdown1 = st.sidebar.selectbox("Pick a Region", regions)
dropdown1 = st.sidebar.selectbox("Pick Analysis Type", atype)

#if region = xx, choose atype, then display atype 4 charts for that region
#con1 = st.container()
#with st.container():
st.plotly_chart(suf, use_container_width=True)
st.plotly_chart(fig18,use_container_width=True)
st.plotly_chart(figdt2)
st.plotly_chart(gmt)


