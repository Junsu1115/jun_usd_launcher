import json
import os
import google.generativeai as genai


class GeminiHandler:
    def __init__(self):
        with open("/Users/junsu/Desktop/jun_usd_helper/core/gemini/gemini_functions.json", "r", encoding="utf-8") as f:
            self.functions = json.load(f)
        api_key = os.environ.get("GEMINI_API_KEY")
        if api_key:
            genai.configure(api_key=api_key)
        else:
            print("[Error] GEMINI_API_KEY 환경 변수가 설정되어 있지 않습니다.")

    def build_gemini_system(self):
        functions_description = []
        for function in self.functions:
            name = function["name"]
            desc = function["description"]
            params = function["parameters"].get("properties", {})
            if params:
                params_list = []
                required = function["parameters"].get("required", [])
                for param_name, param_info in params.items():
                    params_desc = f"{param_name}(string): {param_info.get('description','')}"
                    if param_name in required:
                        params_desc += "[required]"
                    params_list.append(params_desc)
                params_str = "params: " + ", ".join(params_list)
            else:
                params_str = "params: none"
            one_line = f"{name} - {desc} -{params_str}"
            functions_description.append(one_line)

        functions_text = "\n".join(f"- {line}" for line in functions_description)

        system_instruction = f"""
        당신은 AI 함수 호출 어시스턴트입니다.
        또한, 함수 호출 외에도 일반적인 chat bot처럼 질문에 응답할 수 있습니다.
        아래는 사용할 수 있는 함수 목록과 설명입니다:
    
        {functions_text}
    
        사용자의 자연어 요청을 보고,
        반드시 **아래 JSON 형식**으로만 응답하세요:
    
        {{
          "function_call": {{
            "name": "<함수이름>",
            "arguments": {{ 
              // 함수 호출 시 필요한 딕셔너리 형태의 인자
            }}
          }}
        }}
    
        - 만약 사용자 요청이 위 함수들과 관계없다면:
        {{
          "function_call": {{
            "name": "none",
            "arguments": {{ }}
          }}
        }}
        """
        return system_instruction

    def gemini(self):
        system_instruction = self.build_gemini_system()

        user_input = input("명령을 입력해주세요: ")

        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash-preview-05-20",
            system_instruction=system_instruction
        )

        response = model.generate_content(user_input)
        print("--- Gemini Response ---")
        print(response.text)
        print("-----------------------")

if __name__ == '__main__':
    handler = GeminiHandler()
    handler.gemini()

