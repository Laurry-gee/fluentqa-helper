import gradio as gr

from commands.mac_proxy_cli import proxy_off
from commands.api_capture import *


def api_capture_tab():
    with gr.Tab("API Capture"):
        with gr.Row():
            with gr.Column(scale=4):
                inp = gr.Textbox(placeholder="输入本次录制接口访问名称", show_label=False)
            with gr.Column(scale=4):
                capture_btn = gr.Button("开始录制接口访问-API Capture", variant="primary")
                stop_capture_btn = gr.Button("停止录制接口访问-Stop API Capture", variant="primary")
                reset_proxy = gr.Button("重置MAC代理-Reset MAC Proxy Setting", variant="primary")
                capture_btn.click(fn=start, inputs=inp)
                stop_capture_btn.click(fn=stop_capture)
                reset_proxy.click(fn=proxy_off)



def init_ui():
    with gr.Blocks() as qa_tools:
        gr.Markdown("# QA toolkits")
        api_capture_tab()
        # code_generate_tab()

    qa_tools.launch()
