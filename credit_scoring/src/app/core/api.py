from dataclasses import dataclass
from enum import Enum, auto

import numpy as np


class ScoringDecision(Enum):
    """Возможные решения модели."""

    # (добавил, чтобы мр прошёл)
    ACCEPTED = auto()
    DECLINED = auto()


@dataclass
class ScoringResult(object):
    """Класс, содержащий результаты скоринга."""

    decision: ScoringDecision
    amount: int
    threshold: float
    proba: float


@dataclass
class Features(object):
    """Фичи для принятия решения об одобрении."""

    DOCUMENTS_PROVIDED: int = np.nan
    HOME_FEATURE: int = np.nan
    YEARS_OLD: int = np.nan
    YEARS_ID_CHANGED: int = np.nan
    DIFFERENCE_ID_CHANGE_AND_OLDNESS: int = np.nan
    DOCUMENT_CHANGE_DELAY: bool = np.nan
    ANNUITY_TO_INCOME_RATIO: float = np.nan
    CHILDREN_PER_ADULT: float = np.nan
    INC_PER_CHLD: float = np.nan
    INC_PER_ADULT: float = np.nan
    INTEREST_RATE_v1: float = np.nan
    INTEREST_RATE_v2: float = np.nan
    WEIGHTED_EXT_SOURCE: float = np.nan
    DIFFERENCE_OF_INCOME: float = np.nan
    PREV_AMT_ANNUITY_MAX: float = np.nan
    PREV_AMT_ANNUITY_MEAN: float = np.nan
    PREV_AMT_APPLICATION_MAX: float = np.nan
    PREV_AMT_APPLICATION_MEAN: float = np.nan
    PREV_AMT_CREDIT_MAX: float = np.nan
    PREV_AMT_CREDIT_MEAN: float = np.nan
    PREV_APP_CREDIT_PERC_MAX: float = np.nan
    PREV_APP_CREDIT_PERC_MEAN: float = np.nan
    PREV_AMT_DOWN_PAYMENT_MAX: float = np.nan
    PREV_AMT_DOWN_PAYMENT_MEAN: float = np.nan
    PREV_AMT_GOODS_PRICE_MAX: float = np.nan
    PREV_AMT_GOODS_PRICE_MEAN: float = np.nan
    PREV_HOUR_APPR_PROCESS_START_MAX: float = np.nan
    PREV_HOUR_APPR_PROCESS_START_MEAN: float = np.nan
    PREV_RATE_DOWN_PAYMENT_MAX: float = np.nan
    PREV_RATE_DOWN_PAYMENT_MEAN: float = np.nan
    PREV_DAYS_DECISION_MAX: float = np.nan
    PREV_DAYS_DECISION_MEAN: float = np.nan
    PREV_CNT_PAYMENT_MEAN: float = np.nan
    PREV_CNT_PAYMENT_SUM: float = np.nan
    PREV_NAME_CONTRACT_TYPE_Cash_loans_MEAN: float = np.nan
    PREV_NAME_CONTRACT_TYPE_Consumer_loans_MEAN: float = np.nan
    PREV_NAME_CONTRACT_TYPE_Revolving_loans_MEAN: float = np.nan
    PREV_NAME_CONTRACT_TYPE_XNA_MEAN: float = np.nan
    PREV_NAME_CONTRACT_TYPE_nan_MEAN: float = np.nan
    PREV_WEEKDAY_APPR_PROCESS_START_FRIDAY_MEAN: float = np.nan
    PREV_WEEKDAY_APPR_PROCESS_START_MONDAY_MEAN: float = np.nan
    PREV_WEEKDAY_APPR_PROCESS_START_SATURDAY_MEAN: float = np.nan
    PREV_WEEKDAY_APPR_PROCESS_START_SUNDAY_MEAN: float = np.nan
    PREV_WEEKDAY_APPR_PROCESS_START_THURSDAY_MEAN: float = np.nan
    PREV_WEEKDAY_APPR_PROCESS_START_TUESDAY_MEAN: float = np.nan
    PREV_WEEKDAY_APPR_PROCESS_START_WEDNESDAY_MEAN: float = np.nan
    PREV_WEEKDAY_APPR_PROCESS_START_nan_MEAN: float = np.nan
    PREV_FLAG_LAST_APPL_PER_CONTRACT_N_MEAN: float = np.nan
    PREV_FLAG_LAST_APPL_PER_CONTRACT_Y_MEAN: float = np.nan
    PREV_FLAG_LAST_APPL_PER_CONTRACT_nan_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Building_a_house_or_an_annex_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Business_development_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Buying_a_garage_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Buying_a_holiday_home_land_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Buying_a_home_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Buying_a_new_car_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Buying_a_used_car_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Car_repairs_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Education_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Everyday_expenses_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Furniture_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Gasification_water_supply_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Hobby_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Journey_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Medicine_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Money_for_a_third_person_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Other_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Payments_on_other_loans_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Purchase_of_electronic_equipment_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Refusal_to_name_the_goal_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Repairs_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Urgent_needs_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_Wedding_gift_holiday_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_XAP_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_XNA_MEAN: float = np.nan
    PREV_NAME_CASH_LOAN_PURPOSE_nan_MEAN: float = np.nan
    PREV_NAME_CONTRACT_STATUS_Approved_MEAN: float = np.nan
    PREV_NAME_CONTRACT_STATUS_Canceled_MEAN: float = np.nan
    PREV_NAME_CONTRACT_STATUS_Refused_MEAN: float = np.nan
    PREV_NAME_CONTRACT_STATUS_Unused_offer_MEAN: float = np.nan
    PREV_NAME_CONTRACT_STATUS_nan_MEAN: float = np.nan
    PREV_NAME_PAYMENT_TYPE_Cash_through_the_bank_MEAN: float = np.nan
    PREV_NAME_PAYMENT_TYPE_Cashless_from_the_account_of_the_employer_MEAN: float = np.nan
    PREV_NAME_PAYMENT_TYPE_Non_cash_from_your_account_MEAN: float = np.nan
    PREV_NAME_PAYMENT_TYPE_XNA_MEAN: float = np.nan
    PREV_NAME_PAYMENT_TYPE_nan_MEAN: float = np.nan
    PREV_CODE_REJECT_REASON_CLIENT_MEAN: float = np.nan
    PREV_CODE_REJECT_REASON_HC_MEAN: float = np.nan
    PREV_CODE_REJECT_REASON_LIMIT_MEAN: float = np.nan
    PREV_CODE_REJECT_REASON_SCO_MEAN: float = np.nan
    PREV_CODE_REJECT_REASON_SCOFR_MEAN: float = np.nan
    PREV_CODE_REJECT_REASON_SYSTEM_MEAN: float = np.nan
    PREV_CODE_REJECT_REASON_VERIF_MEAN: float = np.nan
    PREV_CODE_REJECT_REASON_XAP_MEAN: float = np.nan
    PREV_CODE_REJECT_REASON_XNA_MEAN: float = np.nan
    PREV_CODE_REJECT_REASON_nan_MEAN: float = np.nan
    PREV_NAME_TYPE_SUITE_Children_MEAN: float = np.nan
    PREV_NAME_TYPE_SUITE_Family_MEAN: float = np.nan
    PREV_NAME_TYPE_SUITE_Group_of_people_MEAN: float = np.nan
    PREV_NAME_TYPE_SUITE_Other_A_MEAN: float = np.nan
    PREV_NAME_TYPE_SUITE_Other_B_MEAN: float = np.nan
    PREV_NAME_TYPE_SUITE_Spouse_partner_MEAN: float = np.nan
    PREV_NAME_TYPE_SUITE_Unaccompanied_MEAN: float = np.nan
    PREV_NAME_TYPE_SUITE_nan_MEAN: float = np.nan
    PREV_NAME_CLIENT_TYPE_New_MEAN: float = np.nan
    PREV_NAME_CLIENT_TYPE_Refreshed_MEAN: float = np.nan
    PREV_NAME_CLIENT_TYPE_Repeater_MEAN: float = np.nan
    PREV_NAME_CLIENT_TYPE_XNA_MEAN: float = np.nan
    PREV_NAME_CLIENT_TYPE_nan_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Additional_Service_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Animals_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Audio_Video_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Auto_Accessories_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Clothing_and_Accessories_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Computers_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Confloatuction_Materials_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Consumer_Electronics_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Direct_Sales_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Education_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Fitness_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Furniture_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Gardening_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Homewares_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_House_Confloatuction_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Insurance_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Jewelry_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Medical_Supplies_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Medicine_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Mobile_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Office_Appliances_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Other_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Photo_Cinema_Equipment_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Sport_and_Leisure_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Tourism_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Vehicles_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_Weapon_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_XNA_MEAN: float = np.nan
    PREV_NAME_GOODS_CATEGORY_nan_MEAN: float = np.nan
    PREV_NAME_PORTFOLIO_Cards_MEAN: float = np.nan
    PREV_NAME_PORTFOLIO_Cars_MEAN: float = np.nan
    PREV_NAME_PORTFOLIO_Cash_MEAN: float = np.nan
    PREV_NAME_PORTFOLIO_POS_MEAN: float = np.nan
    PREV_NAME_PORTFOLIO_XNA_MEAN: float = np.nan
    PREV_NAME_PORTFOLIO_nan_MEAN: float = np.nan
    PREV_NAME_PRODUCT_TYPE_XNA_MEAN: float = np.nan
    PREV_NAME_PRODUCT_TYPE_walk_in_MEAN: float = np.nan
    PREV_NAME_PRODUCT_TYPE_x_sell_MEAN: float = np.nan
    PREV_NAME_PRODUCT_TYPE_nan_MEAN: float = np.nan
    PREV_CHANNEL_TYPE_AP_Cash_loan_MEAN: float = np.nan
    PREV_CHANNEL_TYPE_Car_dealer_MEAN: float = np.nan
    PREV_CHANNEL_TYPE_Channel_of_corporate_sales_MEAN: float = np.nan
    PREV_CHANNEL_TYPE_Contact_center_MEAN: float = np.nan
    PREV_CHANNEL_TYPE_Country_wide_MEAN: float = np.nan
    PREV_CHANNEL_TYPE_Credit_and_cash_offices_MEAN: float = np.nan
    PREV_CHANNEL_TYPE_Regional_Local_MEAN: float = np.nan
    PREV_CHANNEL_TYPE_Stone_MEAN: float = np.nan
    PREV_CHANNEL_TYPE_nan_MEAN: float = np.nan
    PREV_NAME_SELLER_INDUfloatY_Auto_technology_MEAN: float = np.nan
    PREV_NAME_SELLER_INDUfloatY_Clothing_MEAN: float = np.nan
    PREV_NAME_SELLER_INDUfloatY_Connectivity_MEAN: float = np.nan
    PREV_NAME_SELLER_INDUfloatY_Confloatuction_MEAN: float = np.nan
    PREV_NAME_SELLER_INDUfloatY_Consumer_electronics_MEAN: float = np.nan
    PREV_NAME_SELLER_INDUfloatY_Furniture_MEAN: float = np.nan
    PREV_NAME_SELLER_INDUfloatY_Indufloaty_MEAN: float = np.nan
    PREV_NAME_SELLER_INDUfloatY_Jewelry_MEAN: float = np.nan
    PREV_NAME_SELLER_INDUfloatY_MLM_partners_MEAN: float = np.nan
    PREV_NAME_SELLER_INDUfloatY_Tourism_MEAN: float = np.nan
    PREV_NAME_SELLER_INDUfloatY_XNA_MEAN: float = np.nan
    PREV_NAME_SELLER_INDUfloatY_nan_MEAN: float = np.nan
    PREV_NAME_YIELD_GROUP_XNA_MEAN: float = np.nan
    PREV_NAME_YIELD_GROUP_high_MEAN: float = np.nan
    PREV_NAME_YIELD_GROUP_low_action_MEAN: float = np.nan
    PREV_NAME_YIELD_GROUP_low_normal_MEAN: float = np.nan
    PREV_NAME_YIELD_GROUP_middle_MEAN: float = np.nan
    PREV_NAME_YIELD_GROUP_nan_MEAN: float = np.nan
    PREV_PRODUCT_COMBINATION_Card_floateet_MEAN: float = np.nan
    PREV_PRODUCT_COMBINATION_Card_X_Sell_MEAN: float = np.nan
    PREV_PRODUCT_COMBINATION_Cash_MEAN: float = np.nan
    PREV_PRODUCT_COMBINATION_Cash_floateet_high_MEAN: float = np.nan
    PREV_PRODUCT_COMBINATION_Cash_floateet_low_MEAN: float = np.nan
    PREV_PRODUCT_COMBINATION_Cash_floateet_middle_MEAN: float = np.nan
    PREV_PRODUCT_COMBINATION_Cash_X_Sell_high_MEAN: float = np.nan
    PREV_PRODUCT_COMBINATION_Cash_X_Sell_low_MEAN: float = np.nan
    PREV_PRODUCT_COMBINATION_Cash_X_Sell_middle_MEAN: float = np.nan
    PREV_PRODUCT_COMBINATION_POS_household_with_interest_MEAN: float = np.nan
    PREV_PRODUCT_COMBINATION_POS_household_without_interest_MEAN: float = np.nan
    PREV_PRODUCT_COMBINATION_POS_indufloaty_with_interest_MEAN: float = np.nan
    PREV_PRODUCT_COMBINATION_POS_indufloaty_without_interest_MEAN: float = np.nan
    PREV_PRODUCT_COMBINATION_POS_mobile_with_interest_MEAN: float = np.nan
    PREV_PRODUCT_COMBINATION_POS_mobile_without_interest_MEAN: float = np.nan
    PREV_PRODUCT_COMBINATION_POS_other_with_interest_MEAN: float = np.nan
    PREV_PRODUCT_COMBINATION_POS_others_without_interest_MEAN: float = np.nan
    PREV_PRODUCT_COMBINATION_nan_MEAN: float = np.nan
    APPROVED_AMT_ANNUITY_MAX: float = np.nan
    APPROVED_AMT_ANNUITY_MEAN: float = np.nan
    APPROVED_AMT_APPLICATION_MAX: float = np.nan
    APPROVED_AMT_APPLICATION_MEAN: float = np.nan
    APPROVED_AMT_CREDIT_MAX: float = np.nan
    APPROVED_AMT_CREDIT_MEAN: float = np.nan
    APPROVED_APP_CREDIT_PERC_MAX: float = np.nan
    APPROVED_APP_CREDIT_PERC_MEAN: float = np.nan
    APPROVED_AMT_DOWN_PAYMENT_MAX: float = np.nan
    APPROVED_AMT_DOWN_PAYMENT_MEAN: float = np.nan
    APPROVED_AMT_GOODS_PRICE_MAX: float = np.nan
    APPROVED_AMT_GOODS_PRICE_MEAN: float = np.nan
    APPROVED_HOUR_APPR_PROCESS_START_MAX: float = np.nan
    APPROVED_HOUR_APPR_PROCESS_START_MEAN: float = np.nan
    APPROVED_RATE_DOWN_PAYMENT_MAX: float = np.nan
    APPROVED_RATE_DOWN_PAYMENT_MEAN: float = np.nan
    APPROVED_DAYS_DECISION_MAX: float = np.nan
    APPROVED_DAYS_DECISION_MEAN: float = np.nan
    APPROVED_CNT_PAYMENT_MEAN: float = np.nan
    APPROVED_CNT_PAYMENT_SUM: float = np.nan
    REFUSED_AMT_ANNUITY_MAX: float = np.nan
    REFUSED_AMT_ANNUITY_MEAN: float = np.nan
    REFUSED_AMT_APPLICATION_MAX: float = np.nan
    REFUSED_AMT_APPLICATION_MEAN: float = np.nan
    REFUSED_AMT_CREDIT_MAX: float = np.nan
    REFUSED_AMT_CREDIT_MEAN: float = np.nan
    REFUSED_APP_CREDIT_PERC_MAX: float = np.nan
    REFUSED_APP_CREDIT_PERC_MEAN: float = np.nan
    REFUSED_AMT_DOWN_PAYMENT_MAX: float = np.nan
    REFUSED_AMT_DOWN_PAYMENT_MEAN: float = np.nan
    REFUSED_AMT_GOODS_PRICE_MAX: float = np.nan
    REFUSED_AMT_GOODS_PRICE_MEAN: float = np.nan
    REFUSED_HOUR_APPR_PROCESS_START_MAX: float = np.nan
    REFUSED_HOUR_APPR_PROCESS_START_MEAN: float = np.nan
    REFUSED_RATE_DOWN_PAYMENT_MAX: float = np.nan
    REFUSED_RATE_DOWN_PAYMENT_MEAN: float = np.nan
    REFUSED_DAYS_DECISION_MAX: float = np.nan
    REFUSED_DAYS_DECISION_MEAN: float = np.nan
    REFUSED_CNT_PAYMENT_MEAN: float = np.nan
    REFUSED_CNT_PAYMENT_SUM: float = np.nan
    INSTALL_NUM_INSTALMENT_VERSION_NUNIQUE: float = np.nan
    INSTALL_DPD_MAX: float = np.nan
    INSTALL_DPD_MEAN: float = np.nan
    INSTALL_DPD_SUM: float = np.nan
    INSTALL_DPD_MIN: float = np.nan
    INSTALL_DPD_STD: float = np.nan
    INSTALL_DBD_MAX: float = np.nan
    INSTALL_DBD_MEAN: float = np.nan
    INSTALL_DBD_SUM: float = np.nan
    INSTALL_DBD_MIN: float = np.nan
    INSTALL_DBD_STD: float = np.nan
    INSTALL_PAYMENT_PERC_MAX: float = np.nan
    INSTALL_PAYMENT_PERC_MEAN: float = np.nan
    INSTALL_PAYMENT_PERC_VAR: float = np.nan
    INSTALL_PAYMENT_PERC_MIN: float = np.nan
    INSTALL_PAYMENT_PERC_STD: float = np.nan
    INSTALL_PAYMENT_DIFF_MAX: float = np.nan
    INSTALL_PAYMENT_DIFF_MEAN: float = np.nan
    INSTALL_PAYMENT_DIFF_VAR: float = np.nan
    INSTALL_PAYMENT_DIFF_MIN: float = np.nan
    INSTALL_PAYMENT_DIFF_STD: float = np.nan
    INSTALL_AMT_INSTALMENT_MAX: float = np.nan
    INSTALL_AMT_INSTALMENT_MEAN: float = np.nan
    INSTALL_AMT_INSTALMENT_SUM: float = np.nan
    INSTALL_AMT_INSTALMENT_MIN: float = np.nan
    INSTALL_AMT_INSTALMENT_STD: float = np.nan
    INSTALL_AMT_PAYMENT_MIN: float = np.nan
    INSTALL_AMT_PAYMENT_MAX: float = np.nan
    INSTALL_AMT_PAYMENT_MEAN: float = np.nan
    INSTALL_AMT_PAYMENT_SUM: float = np.nan
    INSTALL_AMT_PAYMENT_STD: float = np.nan
    INSTALL_DAYS_ENTRY_PAYMENT_MAX: float = np.nan
    INSTALL_DAYS_ENTRY_PAYMENT_MEAN: float = np.nan
    INSTALL_DAYS_ENTRY_PAYMENT_SUM: float = np.nan
    INSTALL_DAYS_ENTRY_PAYMENT_STD: float = np.nan
    INSTALL_COUNT: float = np.nan
    CC_MONTHS_BALANCE_MAX: float = np.nan
    CC_MONTHS_BALANCE_MIN: float = np.nan
    CC_MONTHS_BALANCE_MEAN: float = np.nan
    CC_MONTHS_BALANCE_MEDIAN: float = np.nan
    CC_MONTHS_BALANCE_SUM: float = np.nan
    CC_MONTHS_BALANCE_VAR: float = np.nan
    CC_AMT_BALANCE_MAX: float = np.nan
    CC_AMT_BALANCE_MIN: float = np.nan
    CC_AMT_BALANCE_MEAN: float = np.nan
    CC_AMT_BALANCE_MEDIAN: float = np.nan
    CC_AMT_BALANCE_SUM: float = np.nan
    CC_AMT_BALANCE_VAR: float = np.nan
    CC_AMT_CREDIT_LIMIT_ACTUAL_MAX: float = np.nan
    CC_AMT_CREDIT_LIMIT_ACTUAL_MIN: float = np.nan
    CC_AMT_CREDIT_LIMIT_ACTUAL_MEAN: float = np.nan
    CC_AMT_CREDIT_LIMIT_ACTUAL_MEDIAN: float = np.nan
    CC_AMT_CREDIT_LIMIT_ACTUAL_SUM: float = np.nan
    CC_AMT_CREDIT_LIMIT_ACTUAL_VAR: float = np.nan
    CC_AMT_DRAWINGS_ATM_CURRENT_MAX: float = np.nan
    CC_AMT_DRAWINGS_ATM_CURRENT_MIN: float = np.nan
    CC_AMT_DRAWINGS_ATM_CURRENT_MEAN: float = np.nan
    CC_AMT_DRAWINGS_ATM_CURRENT_MEDIAN: float = np.nan
    CC_AMT_DRAWINGS_ATM_CURRENT_SUM: float = np.nan
    CC_AMT_DRAWINGS_ATM_CURRENT_VAR: float = np.nan
    CC_AMT_DRAWINGS_CURRENT_MAX: float = np.nan
    CC_AMT_DRAWINGS_CURRENT_MIN: float = np.nan
    CC_AMT_DRAWINGS_CURRENT_MEAN: float = np.nan
    CC_AMT_DRAWINGS_CURRENT_MEDIAN: float = np.nan
    CC_AMT_DRAWINGS_CURRENT_SUM: float = np.nan
    CC_AMT_DRAWINGS_CURRENT_VAR: float = np.nan
    CC_AMT_DRAWINGS_OTHER_CURRENT_MAX: float = np.nan
    CC_AMT_DRAWINGS_OTHER_CURRENT_MIN: float = np.nan
    CC_AMT_DRAWINGS_OTHER_CURRENT_MEAN: float = np.nan
    CC_AMT_DRAWINGS_OTHER_CURRENT_MEDIAN: float = np.nan
    CC_AMT_DRAWINGS_OTHER_CURRENT_SUM: float = np.nan
    CC_AMT_DRAWINGS_OTHER_CURRENT_VAR: float = np.nan
    CC_AMT_DRAWINGS_POS_CURRENT_MAX: float = np.nan
    CC_AMT_DRAWINGS_POS_CURRENT_MIN: float = np.nan
    CC_AMT_DRAWINGS_POS_CURRENT_MEAN: float = np.nan
    CC_AMT_DRAWINGS_POS_CURRENT_MEDIAN: float = np.nan
    CC_AMT_DRAWINGS_POS_CURRENT_SUM: float = np.nan
    CC_AMT_DRAWINGS_POS_CURRENT_VAR: float = np.nan
    CC_AMT_INST_MIN_REGULARITY_MAX: float = np.nan
    CC_AMT_INST_MIN_REGULARITY_MIN: float = np.nan
    CC_AMT_INST_MIN_REGULARITY_MEAN: float = np.nan
    CC_AMT_INST_MIN_REGULARITY_MEDIAN: float = np.nan
    CC_AMT_INST_MIN_REGULARITY_SUM: float = np.nan
    CC_AMT_INST_MIN_REGULARITY_VAR: float = np.nan
    CC_AMT_PAYMENT_CURRENT_MAX: float = np.nan
    CC_AMT_PAYMENT_CURRENT_MIN: float = np.nan
    CC_AMT_PAYMENT_CURRENT_MEAN: float = np.nan
    CC_AMT_PAYMENT_CURRENT_MEDIAN: float = np.nan
    CC_AMT_PAYMENT_CURRENT_SUM: float = np.nan
    CC_AMT_PAYMENT_CURRENT_VAR: float = np.nan
    CC_AMT_PAYMENT_TOTAL_CURRENT_MAX: float = np.nan
    CC_AMT_PAYMENT_TOTAL_CURRENT_MIN: float = np.nan
    CC_AMT_PAYMENT_TOTAL_CURRENT_MEAN: float = np.nan
    CC_AMT_PAYMENT_TOTAL_CURRENT_MEDIAN: float = np.nan
    CC_AMT_PAYMENT_TOTAL_CURRENT_SUM: float = np.nan
    CC_AMT_PAYMENT_TOTAL_CURRENT_VAR: float = np.nan
    CC_AMT_RECEIVABLE_PRINCIPAL_MAX: float = np.nan
    CC_AMT_RECEIVABLE_PRINCIPAL_MIN: float = np.nan
    CC_AMT_RECEIVABLE_PRINCIPAL_MEAN: float = np.nan
    CC_AMT_RECEIVABLE_PRINCIPAL_MEDIAN: float = np.nan
    CC_AMT_RECEIVABLE_PRINCIPAL_SUM: float = np.nan
    CC_AMT_RECEIVABLE_PRINCIPAL_VAR: float = np.nan
    CC_AMT_RECIVABLE_MAX: float = np.nan
    CC_AMT_RECIVABLE_MIN: float = np.nan
    CC_AMT_RECIVABLE_MEAN: float = np.nan
    CC_AMT_RECIVABLE_MEDIAN: float = np.nan
    CC_AMT_RECIVABLE_SUM: float = np.nan
    CC_AMT_RECIVABLE_VAR: float = np.nan
    CC_AMT_TOTAL_RECEIVABLE_MAX: float = np.nan
    CC_AMT_TOTAL_RECEIVABLE_MIN: float = np.nan
    CC_AMT_TOTAL_RECEIVABLE_MEAN: float = np.nan
    CC_AMT_TOTAL_RECEIVABLE_MEDIAN: float = np.nan
    CC_AMT_TOTAL_RECEIVABLE_SUM: float = np.nan
    CC_AMT_TOTAL_RECEIVABLE_VAR: float = np.nan
    CC_CNT_DRAWINGS_ATM_CURRENT_MAX: float = np.nan
    CC_CNT_DRAWINGS_ATM_CURRENT_MIN: float = np.nan
    CC_CNT_DRAWINGS_ATM_CURRENT_MEAN: float = np.nan
    CC_CNT_DRAWINGS_ATM_CURRENT_MEDIAN: float = np.nan
    CC_CNT_DRAWINGS_ATM_CURRENT_SUM: float = np.nan
    CC_CNT_DRAWINGS_ATM_CURRENT_VAR: float = np.nan
    CC_CNT_DRAWINGS_CURRENT_MAX: float = np.nan
    CC_CNT_DRAWINGS_CURRENT_MIN: float = np.nan
    CC_CNT_DRAWINGS_CURRENT_MEAN: float = np.nan
    CC_CNT_DRAWINGS_CURRENT_MEDIAN: float = np.nan
    CC_CNT_DRAWINGS_CURRENT_SUM: float = np.nan
    CC_CNT_DRAWINGS_CURRENT_VAR: float = np.nan
    CC_CNT_DRAWINGS_OTHER_CURRENT_MAX: float = np.nan
    CC_CNT_DRAWINGS_OTHER_CURRENT_MIN: float = np.nan
    CC_CNT_DRAWINGS_OTHER_CURRENT_MEAN: float = np.nan
    CC_CNT_DRAWINGS_OTHER_CURRENT_MEDIAN: float = np.nan
    CC_CNT_DRAWINGS_OTHER_CURRENT_SUM: float = np.nan
    CC_CNT_DRAWINGS_OTHER_CURRENT_VAR: float = np.nan
    CC_CNT_DRAWINGS_POS_CURRENT_MAX: float = np.nan
    CC_CNT_DRAWINGS_POS_CURRENT_MIN: float = np.nan
    CC_CNT_DRAWINGS_POS_CURRENT_MEAN: float = np.nan
    CC_CNT_DRAWINGS_POS_CURRENT_MEDIAN: float = np.nan
    CC_CNT_DRAWINGS_POS_CURRENT_SUM: float = np.nan
    CC_CNT_DRAWINGS_POS_CURRENT_VAR: float = np.nan
    CC_CNT_INSTALMENT_MATURE_CUM_MAX: float = np.nan
    CC_CNT_INSTALMENT_MATURE_CUM_MIN: float = np.nan
    CC_CNT_INSTALMENT_MATURE_CUM_MEAN: float = np.nan
    CC_CNT_INSTALMENT_MATURE_CUM_MEDIAN: float = np.nan
    CC_CNT_INSTALMENT_MATURE_CUM_SUM: float = np.nan
    CC_CNT_INSTALMENT_MATURE_CUM_VAR: float = np.nan
    CC_SK_DPD_MAX: float = np.nan
    CC_SK_DPD_MIN: float = np.nan
    CC_SK_DPD_MEAN: float = np.nan
    CC_SK_DPD_MEDIAN: float = np.nan
    CC_SK_DPD_SUM: float = np.nan
    CC_SK_DPD_VAR: float = np.nan
    CC_SK_DPD_DEF_MAX: float = np.nan
    CC_SK_DPD_DEF_MIN: float = np.nan
    CC_SK_DPD_DEF_MEAN: float = np.nan
    CC_SK_DPD_DEF_MEDIAN: float = np.nan
    CC_SK_DPD_DEF_SUM: float = np.nan
    CC_SK_DPD_DEF_VAR: float = np.nan
    DIFF_CC_MONTHS_BALANCE_MAX: float = np.nan
    DIFF_CC_MONTHS_BALANCE_MIN: float = np.nan
    DIFF_CC_MONTHS_BALANCE_MEAN: float = np.nan
    DIFF_CC_MONTHS_BALANCE_MEDIAN: float = np.nan
    DIFF_CC_MONTHS_BALANCE_SUM: float = np.nan
    DIFF_CC_MONTHS_BALANCE_VAR: float = np.nan
    DIFF_CC_AMT_BALANCE_MAX: float = np.nan
    DIFF_CC_AMT_BALANCE_MIN: float = np.nan
    DIFF_CC_AMT_BALANCE_MEAN: float = np.nan
    DIFF_CC_AMT_BALANCE_MEDIAN: float = np.nan
    DIFF_CC_AMT_BALANCE_SUM: float = np.nan
    DIFF_CC_AMT_BALANCE_VAR: float = np.nan
    DIFF_CC_AMT_CREDIT_LIMIT_ACTUAL_MAX: float = np.nan
    DIFF_CC_AMT_CREDIT_LIMIT_ACTUAL_MIN: float = np.nan
    DIFF_CC_AMT_CREDIT_LIMIT_ACTUAL_MEAN: float = np.nan
    DIFF_CC_AMT_CREDIT_LIMIT_ACTUAL_MEDIAN: float = np.nan
    DIFF_CC_AMT_CREDIT_LIMIT_ACTUAL_SUM: float = np.nan
    DIFF_CC_AMT_CREDIT_LIMIT_ACTUAL_VAR: float = np.nan
    DIFF_CC_AMT_DRAWINGS_ATM_CURRENT_MAX: float = np.nan
    DIFF_CC_AMT_DRAWINGS_ATM_CURRENT_MIN: float = np.nan
    DIFF_CC_AMT_DRAWINGS_ATM_CURRENT_MEAN: float = np.nan
    DIFF_CC_AMT_DRAWINGS_ATM_CURRENT_MEDIAN: float = np.nan
    DIFF_CC_AMT_DRAWINGS_ATM_CURRENT_SUM: float = np.nan
    DIFF_CC_AMT_DRAWINGS_ATM_CURRENT_VAR: float = np.nan
    DIFF_CC_AMT_DRAWINGS_CURRENT_MAX: float = np.nan
    DIFF_CC_AMT_DRAWINGS_CURRENT_MIN: float = np.nan
    DIFF_CC_AMT_DRAWINGS_CURRENT_MEAN: float = np.nan
    DIFF_CC_AMT_DRAWINGS_CURRENT_MEDIAN: float = np.nan
    DIFF_CC_AMT_DRAWINGS_CURRENT_SUM: float = np.nan
    DIFF_CC_AMT_DRAWINGS_CURRENT_VAR: float = np.nan
    DIFF_CC_AMT_DRAWINGS_OTHER_CURRENT_MAX: float = np.nan
    DIFF_CC_AMT_DRAWINGS_OTHER_CURRENT_MIN: float = np.nan
    DIFF_CC_AMT_DRAWINGS_OTHER_CURRENT_MEAN: float = np.nan
    DIFF_CC_AMT_DRAWINGS_OTHER_CURRENT_MEDIAN: float = np.nan
    DIFF_CC_AMT_DRAWINGS_OTHER_CURRENT_SUM: float = np.nan
    DIFF_CC_AMT_DRAWINGS_OTHER_CURRENT_VAR: float = np.nan
    DIFF_CC_AMT_DRAWINGS_POS_CURRENT_MAX: float = np.nan
    DIFF_CC_AMT_DRAWINGS_POS_CURRENT_MIN: float = np.nan
    DIFF_CC_AMT_DRAWINGS_POS_CURRENT_MEAN: float = np.nan
    DIFF_CC_AMT_DRAWINGS_POS_CURRENT_MEDIAN: float = np.nan
    DIFF_CC_AMT_DRAWINGS_POS_CURRENT_SUM: float = np.nan
    DIFF_CC_AMT_DRAWINGS_POS_CURRENT_VAR: float = np.nan
    DIFF_CC_AMT_INST_MIN_REGULARITY_MAX: float = np.nan
    DIFF_CC_AMT_INST_MIN_REGULARITY_MIN: float = np.nan
    DIFF_CC_AMT_INST_MIN_REGULARITY_MEAN: float = np.nan
    DIFF_CC_AMT_INST_MIN_REGULARITY_MEDIAN: float = np.nan
    DIFF_CC_AMT_INST_MIN_REGULARITY_SUM: float = np.nan
    DIFF_CC_AMT_INST_MIN_REGULARITY_VAR: float = np.nan
    DIFF_CC_AMT_PAYMENT_CURRENT_MAX: float = np.nan
    DIFF_CC_AMT_PAYMENT_CURRENT_MIN: float = np.nan
    DIFF_CC_AMT_PAYMENT_CURRENT_MEAN: float = np.nan
    DIFF_CC_AMT_PAYMENT_CURRENT_MEDIAN: float = np.nan
    DIFF_CC_AMT_PAYMENT_CURRENT_SUM: float = np.nan
    DIFF_CC_AMT_PAYMENT_CURRENT_VAR: float = np.nan
    DIFF_CC_AMT_PAYMENT_TOTAL_CURRENT_MAX: float = np.nan
    DIFF_CC_AMT_PAYMENT_TOTAL_CURRENT_MIN: float = np.nan
    DIFF_CC_AMT_PAYMENT_TOTAL_CURRENT_MEAN: float = np.nan
    DIFF_CC_AMT_PAYMENT_TOTAL_CURRENT_MEDIAN: float = np.nan
    DIFF_CC_AMT_PAYMENT_TOTAL_CURRENT_SUM: float = np.nan
    DIFF_CC_AMT_PAYMENT_TOTAL_CURRENT_VAR: float = np.nan
    DIFF_CC_AMT_RECEIVABLE_PRINCIPAL_MAX: float = np.nan
    DIFF_CC_AMT_RECEIVABLE_PRINCIPAL_MIN: float = np.nan
    DIFF_CC_AMT_RECEIVABLE_PRINCIPAL_MEAN: float = np.nan
    DIFF_CC_AMT_RECEIVABLE_PRINCIPAL_MEDIAN: float = np.nan
    DIFF_CC_AMT_RECEIVABLE_PRINCIPAL_SUM: float = np.nan
    DIFF_CC_AMT_RECEIVABLE_PRINCIPAL_VAR: float = np.nan
    DIFF_CC_AMT_RECIVABLE_MAX: float = np.nan
    DIFF_CC_AMT_RECIVABLE_MIN: float = np.nan
    DIFF_CC_AMT_RECIVABLE_MEAN: float = np.nan
    DIFF_CC_AMT_RECIVABLE_MEDIAN: float = np.nan
    DIFF_CC_AMT_RECIVABLE_SUM: float = np.nan
    DIFF_CC_AMT_RECIVABLE_VAR: float = np.nan
    DIFF_CC_AMT_TOTAL_RECEIVABLE_MAX: float = np.nan
    DIFF_CC_AMT_TOTAL_RECEIVABLE_MIN: float = np.nan
    DIFF_CC_AMT_TOTAL_RECEIVABLE_MEAN: float = np.nan
    DIFF_CC_AMT_TOTAL_RECEIVABLE_MEDIAN: float = np.nan
    DIFF_CC_AMT_TOTAL_RECEIVABLE_SUM: float = np.nan
    DIFF_CC_AMT_TOTAL_RECEIVABLE_VAR: float = np.nan
    DIFF_CC_CNT_DRAWINGS_ATM_CURRENT_MAX: float = np.nan
    DIFF_CC_CNT_DRAWINGS_ATM_CURRENT_MIN: float = np.nan
    DIFF_CC_CNT_DRAWINGS_ATM_CURRENT_MEAN: float = np.nan
    DIFF_CC_CNT_DRAWINGS_ATM_CURRENT_MEDIAN: float = np.nan
    DIFF_CC_CNT_DRAWINGS_ATM_CURRENT_SUM: float = np.nan
    DIFF_CC_CNT_DRAWINGS_ATM_CURRENT_VAR: float = np.nan
    DIFF_CC_CNT_DRAWINGS_CURRENT_MAX: float = np.nan
    DIFF_CC_CNT_DRAWINGS_CURRENT_MIN: float = np.nan
    DIFF_CC_CNT_DRAWINGS_CURRENT_MEAN: float = np.nan
    DIFF_CC_CNT_DRAWINGS_CURRENT_MEDIAN: float = np.nan
    DIFF_CC_CNT_DRAWINGS_CURRENT_SUM: float = np.nan
    DIFF_CC_CNT_DRAWINGS_CURRENT_VAR: float = np.nan
    DIFF_CC_CNT_DRAWINGS_OTHER_CURRENT_MAX: float = np.nan
    DIFF_CC_CNT_DRAWINGS_OTHER_CURRENT_MIN: float = np.nan
    DIFF_CC_CNT_DRAWINGS_OTHER_CURRENT_MEAN: float = np.nan
    DIFF_CC_CNT_DRAWINGS_OTHER_CURRENT_MEDIAN: float = np.nan
    DIFF_CC_CNT_DRAWINGS_OTHER_CURRENT_SUM: float = np.nan
    DIFF_CC_CNT_DRAWINGS_OTHER_CURRENT_VAR: float = np.nan
    DIFF_CC_CNT_DRAWINGS_POS_CURRENT_MAX: float = np.nan
    DIFF_CC_CNT_DRAWINGS_POS_CURRENT_MIN: float = np.nan
    DIFF_CC_CNT_DRAWINGS_POS_CURRENT_MEAN: float = np.nan
    DIFF_CC_CNT_DRAWINGS_POS_CURRENT_MEDIAN: float = np.nan
    DIFF_CC_CNT_DRAWINGS_POS_CURRENT_SUM: float = np.nan
    DIFF_CC_CNT_DRAWINGS_POS_CURRENT_VAR: float = np.nan
    DIFF_CC_CNT_INSTALMENT_MATURE_CUM_MAX: float = np.nan
    DIFF_CC_CNT_INSTALMENT_MATURE_CUM_MIN: float = np.nan
    DIFF_CC_CNT_INSTALMENT_MATURE_CUM_MEAN: float = np.nan
    DIFF_CC_CNT_INSTALMENT_MATURE_CUM_MEDIAN: float = np.nan
    DIFF_CC_CNT_INSTALMENT_MATURE_CUM_SUM: float = np.nan
    DIFF_CC_CNT_INSTALMENT_MATURE_CUM_VAR: float = np.nan
    DIFF_CC_SK_DPD_MAX: float = np.nan
    DIFF_CC_SK_DPD_MIN: float = np.nan
    DIFF_CC_SK_DPD_MEAN: float = np.nan
    DIFF_CC_SK_DPD_MEDIAN: float = np.nan
    DIFF_CC_SK_DPD_SUM: float = np.nan
    DIFF_CC_SK_DPD_VAR: float = np.nan
    DIFF_CC_SK_DPD_DEF_MAX: float = np.nan
    DIFF_CC_SK_DPD_DEF_MIN: float = np.nan
    DIFF_CC_SK_DPD_DEF_MEAN: float = np.nan
    DIFF_CC_SK_DPD_DEF_MEDIAN: float = np.nan
    DIFF_CC_SK_DPD_DEF_SUM: float = np.nan
    DIFF_CC_SK_DPD_DEF_VAR: float = np.nan
    BUREAU_AMT_CREDIT_SUM_DEBT_MAX: float = np.nan
    BUREAU_AMT_CREDIT_SUM_DEBT_MIN: float = np.nan
    DEBT_RATIO: float = np.nan
    CREDIT_TYPE_Another_type_of_loan: float = np.nan
    CREDIT_TYPE_Car_loan: float = np.nan
    CREDIT_TYPE_Cash_loan_non_earmarked: float = np.nan
    CREDIT_TYPE_Consumer_credit: float = np.nan
    CREDIT_TYPE_Credit_card: float = np.nan
    CREDIT_TYPE_Interbank_credit: float = np.nan
    CREDIT_TYPE_Loan_for_business_development: float = np.nan
    CREDIT_TYPE_Loan_for_purchase_of_shares_margin_lending: float = np.nan
    CREDIT_TYPE_Loan_for_the_purchase_of_equipment: float = np.nan
    CREDIT_TYPE_Loan_for_working_capital_replenishment: float = np.nan
    CREDIT_TYPE_Microloan: float = np.nan
    CREDIT_TYPE_Mobile_operator_loan: float = np.nan
    CREDIT_TYPE_Mortgage: float = np.nan
    CREDIT_TYPE_Real_estate_loan: float = np.nan
    CREDIT_TYPE_Unknown_type_of_loan: float = np.nan
    QUESTION_5_ANOTHER_TYPE_OF_LOAN: float = np.nan
    QUESTION_5_CAR_LOAN: float = np.nan
    QUESTION_5_CASH_LOAN_NON_EARMARKED: float = np.nan
    QUESTION_5_CONSUMER_CREDIT: float = np.nan
    QUESTION_5_CREDIT_CARD: float = np.nan
    QUESTION_5_INTERBANK_CREDIT: float = np.nan
    QUESTION_5_LOAN_FOR_BUSINESS_DEVELOPMENT: float = np.nan
    QUESTION_5_LOAN_FOR_THE_PURCHASE_OF_EQUIPMENT: float = np.nan
    QUESTION_5_LOAN_FOR_WORKING_CAPITAL_REPLENISHMENT: float = np.nan
    QUESTION_5_MICROLOAN: float = np.nan
    QUESTION_5_MORTGAGE: float = np.nan
    QUESTION_5_REAL_ESTATE_LOAN: float = np.nan
    QUESTION_5_UNKNOWN_TYPE_OF_LOAN: float = np.nan
    QUESTION_6_ANOTHER_TYPE_OF_LOAN: float = np.nan
    QUESTION_6_CAR_LOAN: float = np.nan
    QUESTION_6_CONSUMER_CREDIT: float = np.nan
    QUESTION_6_CREDIT_CARD: float = np.nan
    QUESTION_6_INTERBANK_CREDIT: float = np.nan
    QUESTION_6_LOAN_FOR_BUSINESS_DEVELOPMENT: float = np.nan
    QUESTION_6_LOAN_FOR_THE_PURCHASE_OF_EQUIPMENT: float = np.nan
    QUESTION_6_LOAN_FOR_WORKING_CAPITAL_REPLENISHMENT: float = np.nan
    QUESTION_6_MICROLOAN: float = np.nan
    QUESTION_6_MORTGAGE: float = np.nan
    QUESTION_6_UNKNOWN_TYPE_OF_LOAN: float = np.nan
    QUESTION_6_ANOTHER_TYPE_OF_LOAN_1: float = np.nan
    QUESTION_6_CAR_LOAN_1: float = np.nan
    QUESTION_6_CONSUMER_CREDIT_1: float = np.nan
    QUESTION_6_CREDIT_CARD_1: float = np.nan
    QUESTION_6_INTERBANK_CREDIT_1: float = np.nan
    QUESTION_6_LOAN_FOR_BUSINESS_DEVELOPMENT_1: float = np.nan
    QUESTION_6_LOAN_FOR_THE_PURCHASE_OF_EQUIPMENT_1: float = np.nan
    QUESTION_6_LOAN_FOR_WORKING_CAPITAL_REPLENISHMENT_1: float = np.nan
    QUESTION_6_MICROLOAN_1: float = np.nan
    QUESTION_6_MORTGAGE_1: float = np.nan
    QUESTION_6_UNKNOWN_TYPE_OF_LOAN_1: float = np.nan
    QUESTION_6_ANOTHER_TYPE_OF_LOAN_2: float = np.nan
    QUESTION_6_CAR_LOAN_2: float = np.nan
    QUESTION_6_CONSUMER_CREDIT_2: float = np.nan
    QUESTION_6_CREDIT_CARD_2: float = np.nan
    QUESTION_6_INTERBANK_CREDIT_2: float = np.nan
    QUESTION_6_LOAN_FOR_BUSINESS_DEVELOPMENT_2: float = np.nan
    QUESTION_6_LOAN_FOR_THE_PURCHASE_OF_EQUIPMENT_2: float = np.nan
    QUESTION_6_LOAN_FOR_WORKING_CAPITAL_REPLENISHMENT_2: float = np.nan
    QUESTION_6_MICROLOAN_2: float = np.nan
    QUESTION_6_MORTGAGE_2: float = np.nan
    QUESTION_6_UNKNOWN_TYPE_OF_LOAN_2: float = np.nan
    QUESTION_6_ANOTHER_TYPE_OF_LOAN_3: float = np.nan
    QUESTION_6_CAR_LOAN_3: float = np.nan
    QUESTION_6_CONSUMER_CREDIT_3: float = np.nan
    QUESTION_6_CREDIT_CARD_3: float = np.nan
    QUESTION_6_INTERBANK_CREDIT_3: float = np.nan
    QUESTION_6_LOAN_FOR_BUSINESS_DEVELOPMENT_3: float = np.nan
    QUESTION_6_LOAN_FOR_THE_PURCHASE_OF_EQUIPMENT_3: float = np.nan
    QUESTION_6_LOAN_FOR_WORKING_CAPITAL_REPLENISHMENT_3: float = np.nan
    QUESTION_6_MICROLOAN_3: float = np.nan
    QUESTION_6_MORTGAGE_3: float = np.nan
    QUESTION_6_UNKNOWN_TYPE_OF_LOAN_3: float = np.nan
    QUESTION_6_ANOTHER_TYPE_OF_LOAN_4: float = np.nan
    QUESTION_6_CAR_LOAN_4: float = np.nan
    QUESTION_6_CONSUMER_CREDIT_4: float = np.nan
    QUESTION_6_CREDIT_CARD_4: float = np.nan
    QUESTION_6_INTERBANK_CREDIT_4: float = np.nan
    QUESTION_6_LOAN_FOR_BUSINESS_DEVELOPMENT_4: float = np.nan
    QUESTION_6_LOAN_FOR_THE_PURCHASE_OF_EQUIPMENT_4: float = np.nan
    QUESTION_6_LOAN_FOR_WORKING_CAPITAL_REPLENISHMENT_4: float = np.nan
    QUESTION_6_MICROLOAN_4: float = np.nan
    QUESTION_6_MORTGAGE_4: float = np.nan
    QUESTION_6_UNKNOWN_TYPE_OF_LOAN_4: float = np.nan
    QUESTION_6_ANOTHER_TYPE_OF_LOAN_5: float = np.nan
    QUESTION_6_CAR_LOAN_5: float = np.nan
    QUESTION_6_CONSUMER_CREDIT_5: float = np.nan
    QUESTION_6_CREDIT_CARD_5: float = np.nan
    QUESTION_6_INTERBANK_CREDIT_5: float = np.nan
    QUESTION_6_LOAN_FOR_BUSINESS_DEVELOPMENT_5: float = np.nan
    QUESTION_6_LOAN_FOR_THE_PURCHASE_OF_EQUIPMENT_5: float = np.nan
    QUESTION_6_LOAN_FOR_WORKING_CAPITAL_REPLENISHMENT_5: float = np.nan
    QUESTION_6_MICROLOAN_5: float = np.nan
    QUESTION_6_MORTGAGE_5: float = np.nan
    QUESTION_6_UNKNOWN_TYPE_OF_LOAN_5: float = np.nan
    QUESTION_6_ANOTHER_TYPE_OF_LOAN_6: float = np.nan
    QUESTION_6_CAR_LOAN_6: float = np.nan
    QUESTION_6_CONSUMER_CREDIT_6: float = np.nan
    QUESTION_6_CREDIT_CARD_6: float = np.nan
    QUESTION_6_INTERBANK_CREDIT_6: float = np.nan
    QUESTION_6_LOAN_FOR_BUSINESS_DEVELOPMENT_6: float = np.nan
    QUESTION_6_LOAN_FOR_THE_PURCHASE_OF_EQUIPMENT_6: float = np.nan
    QUESTION_6_LOAN_FOR_WORKING_CAPITAL_REPLENISHMENT_6: float = np.nan
    QUESTION_6_MICROLOAN_6: float = np.nan
    QUESTION_6_MORTGAGE_6: float = np.nan
    QUESTION_6_UNKNOWN_TYPE_OF_LOAN_6: float = np.nan
    QUESTION_6_ANOTHER_TYPE_OF_LOAN_7: float = np.nan
    QUESTION_6_CAR_LOAN_7: float = np.nan
    QUESTION_6_CONSUMER_CREDIT_7: float = np.nan
    QUESTION_6_CREDIT_CARD_7: float = np.nan
    QUESTION_6_INTERBANK_CREDIT_7: float = np.nan
    QUESTION_6_LOAN_FOR_BUSINESS_DEVELOPMENT_7: float = np.nan
    QUESTION_6_LOAN_FOR_THE_PURCHASE_OF_EQUIPMENT_7: float = np.nan
    QUESTION_6_LOAN_FOR_WORKING_CAPITAL_REPLENISHMENT_7: float = np.nan
    QUESTION_6_MICROLOAN_7: float = np.nan
    QUESTION_6_MORTGAGE_7: float = np.nan
    QUESTION_6_UNKNOWN_TYPE_OF_LOAN_7: float = np.nan
    QUESTION_6_ANOTHER_TYPE_OF_LOAN_8: float = np.nan
    QUESTION_6_CAR_LOAN_8: float = np.nan
    QUESTION_6_CONSUMER_CREDIT_8: float = np.nan
    QUESTION_6_CREDIT_CARD_8: float = np.nan
    QUESTION_6_INTERBANK_CREDIT_8: float = np.nan
    QUESTION_6_LOAN_FOR_BUSINESS_DEVELOPMENT_8: float = np.nan
    QUESTION_6_LOAN_FOR_THE_PURCHASE_OF_EQUIPMENT_8: float = np.nan
    QUESTION_6_LOAN_FOR_WORKING_CAPITAL_REPLENISHMENT_8: float = np.nan
    QUESTION_6_MICROLOAN_8: float = np.nan
    QUESTION_6_MORTGAGE_8: float = np.nan
    QUESTION_6_UNKNOWN_TYPE_OF_LOAN_8: float = np.nan
    QUESTION_6_ANOTHER_TYPE_OF_LOAN_9: float = np.nan
    QUESTION_6_CAR_LOAN_9: float = np.nan
    QUESTION_6_CONSUMER_CREDIT_9: float = np.nan
    QUESTION_6_CREDIT_CARD_9: float = np.nan
    QUESTION_6_INTERBANK_CREDIT_9: float = np.nan
    QUESTION_6_LOAN_FOR_BUSINESS_DEVELOPMENT_9: float = np.nan
    QUESTION_6_LOAN_FOR_THE_PURCHASE_OF_EQUIPMENT_9: float = np.nan
    QUESTION_6_LOAN_FOR_WORKING_CAPITAL_REPLENISHMENT_9: float = np.nan
    QUESTION_6_MICROLOAN_9: float = np.nan
    QUESTION_6_MORTGAGE_9: float = np.nan
    QUESTION_6_UNKNOWN_TYPE_OF_LOAN_9: float = np.nan
    QUESTION_6_ANOTHER_TYPE_OF_LOAN_10: float = np.nan
    QUESTION_6_CAR_LOAN_10: float = np.nan
    QUESTION_6_CONSUMER_CREDIT_10: float = np.nan
    QUESTION_6_CREDIT_CARD_10: float = np.nan
    QUESTION_6_INTERBANK_CREDIT_10: float = np.nan
    QUESTION_6_LOAN_FOR_BUSINESS_DEVELOPMENT_10: float = np.nan
    QUESTION_6_LOAN_FOR_THE_PURCHASE_OF_EQUIPMENT_10: float = np.nan
    QUESTION_6_LOAN_FOR_WORKING_CAPITAL_REPLENISHMENT_10: float = np.nan
    QUESTION_6_MICROLOAN_10: float = np.nan
    QUESTION_6_MORTGAGE_10: float = np.nan
    QUESTION_6_UNKNOWN_TYPE_OF_LOAN_10: float = np.nan
    QUESTION_6_ANOTHER_TYPE_OF_LOAN_11: float = np.nan
    QUESTION_6_CAR_LOAN_11: float = np.nan
    QUESTION_6_CONSUMER_CREDIT_11: float = np.nan
    QUESTION_6_CREDIT_CARD_11: float = np.nan
    QUESTION_6_INTERBANK_CREDIT_11: float = np.nan
    QUESTION_6_LOAN_FOR_BUSINESS_DEVELOPMENT_11: float = np.nan
    QUESTION_6_LOAN_FOR_THE_PURCHASE_OF_EQUIPMENT_11: float = np.nan
    QUESTION_6_LOAN_FOR_WORKING_CAPITAL_REPLENISHMENT_11: float = np.nan
    QUESTION_6_MICROLOAN_11: float = np.nan
    QUESTION_6_MORTGAGE_11: float = np.nan
    QUESTION_6_UNKNOWN_TYPE_OF_LOAN_11: float = np.nan
    QUESTION_6_ANOTHER_TYPE_OF_LOAN_12: float = np.nan
    QUESTION_6_CAR_LOAN_12: float = np.nan
    QUESTION_6_CONSUMER_CREDIT_12: float = np.nan
    QUESTION_6_CREDIT_CARD_12: float = np.nan
    QUESTION_6_INTERBANK_CREDIT_12: float = np.nan
    QUESTION_6_LOAN_FOR_BUSINESS_DEVELOPMENT_12: float = np.nan
    QUESTION_6_LOAN_FOR_THE_PURCHASE_OF_EQUIPMENT_12: float = np.nan
    QUESTION_6_LOAN_FOR_WORKING_CAPITAL_REPLENISHMENT_12: float = np.nan
    QUESTION_6_MICROLOAN_12: float = np.nan
    QUESTION_6_MORTGAGE_12: float = np.nan
    QUESTION_6_UNKNOWN_TYPE_OF_LOAN_12: float = np.nan
    QUESTION_6_ANOTHER_TYPE_OF_LOAN__3: float = np.nan
    QUESTION_6_CAR_LOAN__3: float = np.nan
    QUESTION_6_CONSUMER_CREDIT__3: float = np.nan
    QUESTION_6_CREDIT_CARD__3: float = np.nan
    QUESTION_6_INTERBANK_CREDIT__3: float = np.nan
    QUESTION_6_LOAN_FOR_BUSINESS_DEVELOPMENT__3: float = np.nan
    QUESTION_6_LOAN_FOR_THE_PURCHASE_OF_EQUIPMENT__3: float = np.nan
    QUESTION_6_LOAN_FOR_WORKING_CAPITAL_REPLENISHMENT__3: float = np.nan
    QUESTION_6_MICROLOAN__3: float = np.nan
    QUESTION_6_MORTGAGE__3: float = np.nan
    QUESTION_6_UNKNOWN_TYPE_OF_LOAN__3: float = np.nan
    CREDIT_ACTIVE_Active: float = np.nan
    CREDIT_ACTIVE_Closed: float = np.nan
    AMOUNT_OF_CREDITS: float = np.nan
    RATIO_OF_ACTIVE: float = np.nan
    RATIO_OF_CLOSED: float = np.nan
    STATUS_MAX__0: float = np.nan
    STATUS_MAX__1: float = np.nan
    STATUS_MAX__2: float = np.nan
    STATUS_MAX__3: float = np.nan
    STATUS_MAX__4: float = np.nan
    STATUS_MAX__5: float = np.nan
    RATIO_STATUS_0: float = np.nan
    RATIO_STATUS_1: float = np.nan
    RATIO_STATUS_2: float = np.nan
    RATIO_STATUS_3: float = np.nan
    RATIO_STATUS_4: float = np.nan
    RATIO_STATUS_5: float = np.nan
    CLOSED_MINUS_CURRENT: float = np.nan
    QUESTION_9_BUREAU: float = np.nan
