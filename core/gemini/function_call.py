class FunctionCall:
    @staticmethod
    def run_create_usd():
        """
        사용자 요청이 '퍼블리시' 인 경우 호출됩니다.
        Maya 씬을 USD로 export하는 전체 로직을 수행합니다.
        """
        try:
            from core.export.export_usd import create_usd
            create_usd()
            print("[FunctionCall] run_create_usd() 실행 완료")
        except Exception as e:
            print("[FunctionCall] run_create_usd() 실패:", e)