class CompanyInterface:
    @staticmethod
    def get_company_by_website(*, website: str):
        raise NotImplemented

    @staticmethod
    def create_company(*, name: str, website: str):
        raise NotImplemented
