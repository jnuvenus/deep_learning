import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split

data = pd.read_table('crm_order_item_flow.txt', header=None)
data.columns = ['uid', 'item_id', 'brand_id', 'cate_id', 'time_id']

uid = pd.DataFrame(data.drop_duplicates(['uid'])['uid'])

Train_uid, Test_uid = train_test_split(uid, test_size=0.2)
Train_data = data.merge(Train_uid, on='uid', how='inner')
Test_data = data.merge(Test_uid, on='uid', how='inner')

Train_data.to_csv('Traindata.csv', index=False)
Test_data.to_csv('Testdata.csv', index=False)

feature = pd.read_table('crm_order_train_data20180104.txt', header=None)
feature.columns = ['uid', 'label',
                   'shopping_middle_sort_num',
                   'shopping_max_sort_num',
                   'shopping_brand_num',
                   'shopping_address_num',
                   'search_7_days_pc',
                   'search_7_days_m',
                   'search_7_days_app',
                   'search_30_days_pc',
                   'search_30_days_m',
                   'search_30_days_app',
                   'search_30_days',
                   'lastest_view_time_pc',
                   'lastest_view_time_m',
                   'lastest_view_time_app',
                   'lastest_view_time',
                   'lastest_search_time_pc',
                   'lastest_search_time_m',
                   'lastest_search_time_app',
                   'lastest_search_time',
                   'lastest_add_sc_time_pc',
                   'lastest_add_sc_time_m',
                   'lastest_add_sc_time_app',
                   'lastest_add_sc_time',
                   'is_same_order_reg',
                   'is_instalment',
                   'Îcrm__crm_rfm_total__max_pay_amount',
                   'crm__crm_yohobi__yohobi_toexpire_amount',
                   'crm__crm_yohobi__yohobi_expired_amount',
                   'crm__crm_yohobi__yohobi_available_amount',
                   'crm__crm_vip_upgrade_amount__vip_upgrade_amount',
                   'crm__crm_vip_degrade__last_7_days_vip_degrade',
                   'crm__crm_vip_degrade__last_1_month_vip_degrade',
                   'crm__crm_user_wechat_info__we_chat',
                   'crm__crm_user_vipinfo_iscomplete__is_complete',
                   'crm__crm_user_value_info__p_class',
                   'crm__crm_user_value_info__isold',
                   'crm__crm_user_value_info__d_class',
                   'crm__crm_user_value_info__classstring',
                   'crm__crm_user_value_info__buyagain',
                   'crm__crm_user_value_info__a_class',
                   'crm__crm_user_sign_tags__last_7_days_sign_cnt',
                   'crm__crm_user_sign_tags__last_3_month_sign_cnt',
                   'crm__crm_user_sign_tags__last_1_month_sign_cnt',
                   'crm__crm_user_comment_tags__last_7_days_shareorder_cnt',
                   'crm__crm_user_comment_tags__last_7_days_comment_cnt',
                   'crm__crm_user_comment_tags__last_3_month_shareorder_cnt',
                   'crm__crm_user_comment_tags__last_3_month_comment_cnt',
                   'crm__crm_user_comment_tags__last_1_month_shareorder_cnt',
                   'crm__crm_user_comment_tags__last_1_month_comment_cnt',
                   'crm__crm_user_channel_tags__user_channel',
                   'crm__crm_shopping_cart_tags__retendtiondays',
                   'crm__crm_rfm_total__per_transaction_amount',
                   'crm__crm_rfm_total__pay_amount',
                   'crm__crm_rfm_total__order_count',
                   'crm__crm_rfm_total__order_amount',
                   'crm__crm_rfm_total__max_order_amount',
                   'crm__crm_rfm_total__last_order_tonow',
                   'crm__crm_rfm_total__first_second_order_interval',
                   'crm__crm_rfm_total__first_order_tonow',
                   'crm__crm_rfm_91_days__per_transaction_amount',
                   'crm__crm_rfm_91_days__pay_amount',
                   'crm__crm_rfm_91_days__order_count',
                   'crm__crm_rfm_91_days__order_amount',
                   'crm__crm_rfm_91_days__max_pay_amount',
                   'crm__crm_rfm_91_days__max_order_amount',
                   'crm__crm_rfm_7_days__order_count',
                   'crm__crm_rfm_30_days__per_transaction_amount',
                   'crm__crm_rfm_30_days__pay_amount',
                   'crm__crm_rfm_30_days__order_count',
                   'crm__crm_rfm_30_days__order_amount',
                   'crm__crm_rfm_30_days__max_pay_amount',
                   'crm__crm_rfm_30_days__max_order_amount',
                   'crm__crm_install__install_client',
                   'crm__crm_click_view_feature__last_7days_view_cnt_wap',
                   'crm__crm_click_view_feature__last_7days_view_cnt_pc',
                   'crm__crm_click_view_feature__last_7days_view_cnt_app',
                   'crm__crm_click_view_feature__last_7days_view_cnt',
                   'crm__crm_click_view_feature__last_30days_view_cnt_wap',
                   'crm__crm_click_view_feature__last_30days_view_cnt_pc',
                   'crm__crm_click_view_feature__last_30days_view_cnt_app',
                   'crm__crm_click_view_feature__last_30days_view_cnt',
                   'crm__crm_cart_reduce_tags__cart_reduce_tag',
                   'crm__crm_campaign_tags__last_month_yoho_coin_amount',
                   'crm__crm_campaign_tags__last_month_push_cnt',
                   'crm__crm_campaign_tags__last_month_msg_cnt',
                   'crm__crm_campaign_tags__last_month_coupons_cnt',
                   'crm__crm_campaign_tags__last_3month_yoho_coin_amount',
                   'crm__crm_campaign_tags__last_3month_push_cnt',
                   'crm__crm_campaign_tags__last_3month_msg_cnt',
                   'crm__crm_campaign_tags__last_3month_coupons_cnt',
                   'crm__crm_campaign_tags__available_coupons_cnt',
                   'crm__crm_buy_gender_tags__max_gender',
                   'crm__crm_basic_tags_add__birthday_tonow',
                   'crm__crm_basic_tags__vipdays',
                   'crm__crm_basic_tags__vip_level',
                   'crm__crm_basic_tags__reg_device',
                   'crm__crm_basic_tags__reg_days',
                   'crm__crm_basic_tags__is_student',
                   'crm__crm_basic_tags__gender',
                   'crm__crm_basic_tags__customer_flag',
                   'crm__crm_basic_tags__age',
                   'add_sc_7_days_pc',
                   'add_sc_7_days_m',
                   'add_sc_7_days_app',
                   'add_sc_30_days_pc',
                   'add_sc_30_days_m',
                   'add_sc_30_days_app',
                   'add_sc_30_days']

