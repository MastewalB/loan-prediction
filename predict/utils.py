# r_d = {
#     "gender": "Male",
#     "married":  "Yes",
#     "dependents": 2,
#     "education":   "Graduate",
#     "self_employed": "Yes",
#     "applicant_income": 12000,
#     "coapplicant_income": 10000,
#     "loan_amount": 20000,
#     "loan_amount_term": 360,
#     "credit_history": 1,
#     "property_area": "Urban"
# }


class LoanMapper:
    @staticmethod
    def loan_mapper(raw_data):
        raw_data = {key: LoanMapper.mapper(
            [key, value]) for key, value in raw_data.items()}

        return [raw_data[key] for key in raw_data.keys()]

    @staticmethod
    def mapper(in_dict):
        response_map = {
            "gender": ["Male", "Female"],
            "married": ["No", "Yes"],
            "education": ["Not Graduate", "Graduate"],
            "self_employed": ["No", "Yes"],
            "property_area": ["Urban", "Rural", "Semiurban"]
        }

        if response_map.get(in_dict[0]):
            return response_map[in_dict[0]].index(in_dict[1])
        else:
            return in_dict[1]
