import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer,format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title('Rating Graph')
    plt.pie(x,y)
    plt.tight_layout()
    graph=get_graph()
    return graph


def get_plot9(x,y,z):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,7))
    # plt.title('items vs price')
    plt.plot(x,y)
    cols = ['c','m','r','g','b','y']
    print(len(x))
    plt.pie(y,labels=x,colors=cols,startangle=90,shadow=True,explode=(0.2,0.1,0,0.1,0,0.1,0),autopct='%1.1f%%')
    plt.xticks(rotation=90)
    # plt.legend(x)
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_plot10(x,y,z):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,7))
    # plt.title('items vs price')
    plt.plot(x,y)
    cols = ['c','m','r','g','b','y']
    print(len(x))
    plt.pie(y,labels=x,colors=cols,startangle=90,shadow=True,explode=
    (0.2,0.1,0,0.2,0.1,0,0.2,0.1,0,0.2,0.1,0,0.2,0.1,0,0.2,0.1,0,0.2,0.1,0,0.2),autopct='%1.1f%%')
    plt.xticks(rotation=90)
    # plt.legend(x)
    plt.tight_layout()
    graph = get_graph()
    return graph