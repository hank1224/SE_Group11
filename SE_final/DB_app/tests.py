from django.test import TestCase
from django.contrib.auth.models import User
from django.utils.timezone import localtime, now
from datetime import datetime
from pytz import timezone
from .models import Customers, MassageChairRecord, PhysicalStores, Salespeople, ReferralCodes, Products, OnlineStoreVisits, MassageChairs, MassageChairModes, SalesRecords, SalesQuestionnaires, ExperienceQuestionnaires, ExperienceReservations

timezone_taipei = timezone('Asia/Taipei')
current_time = localtime(now(), timezone_taipei)

class ModelsTestCase(TestCase):
    def setUp(self):
        # Customers
        user1 = User.objects.create_user('user1', password='pass1')
        user2 = User.objects.create_user('user2', password='pass2')
        user3 = User.objects.create_user('user3', password='pass3')
        user4 = User.objects.create_user('user4', password='pass4')
        user5 = User.objects.create_user('user5', password='pass5')
        customer1 = Customers.objects.create(username=user1, customer_name='User One', customer_gender='1', phone_number='12345678')
        customer2 = Customers.objects.create(username=user2, customer_name='User Two', customer_gender='2', phone_number='23456789')
        customer3 = Customers.objects.create(username=user3, customer_name='User Three', customer_gender='3', phone_number='34567890')
        customer4 = Customers.objects.create(username=user4, customer_name='User Four', customer_gender='4', phone_number='45678901')
        customer5 = Customers.objects.create(username=user5, customer_name='User Five', customer_gender='1', phone_number='56789012')
        
        # PhysicalStores
        store1 = PhysicalStores.objects.create(branch_name='Store One')
        store2 = PhysicalStores.objects.create(branch_name='Store Two')
        store3 = PhysicalStores.objects.create(branch_name='Store Three')
        store4 = PhysicalStores.objects.create(branch_name='Store Four')
        store5 = PhysicalStores.objects.create(branch_name='Store Five')
        
        # Salespeople
        salesperson1 = Salespeople.objects.create(salesperson_name='Salesperson One', store_id=store1)
        salesperson2 = Salespeople.objects.create(salesperson_name='Salesperson Two', store_id=store2)
        salesperson3 = Salespeople.objects.create(salesperson_name='Salesperson Three', store_id=store3)
        salesperson4 = Salespeople.objects.create(salesperson_name='Salesperson Four', store_id=store4)
        salesperson5 = Salespeople.objects.create(salesperson_name='Salesperson Five', store_id=store5)
        
        # Products
        product1 = Products.objects.create(product_model='Model One', product_name='Product One', product_price=10000, product_cost=5000, product_warranty=False)
        product2 = Products.objects.create(product_model='Model Two', product_name='Product Two', product_price=20000, product_cost=10000, product_warranty=True)
        product3 = Products.objects.create(product_model='Model Three', product_name='Product Three', product_price=30000, product_cost=15000, product_warranty=False)
        product4 = Products.objects.create(product_model='Model Four', product_name='Product Four', product_price=40000, product_cost=20000, product_warranty=True)
        product5 = Products.objects.create(product_model='Model Five', product_name='Product Five', product_price=50000, product_cost=25000, product_warranty=False)
        
        # MassageChairs
        massage_chair1 = MassageChairs.objects.create(store_id=store1, product_model=product1)
        massage_chair2 = MassageChairs.objects.create(store_id=store2, product_model=product2)
        massage_chair3 = MassageChairs.objects.create(store_id=store3, product_model=product3)
        massage_chair4 = MassageChairs.objects.create(store_id=store4, product_model=product4)
        massage_chair5 = MassageChairs.objects.create(store_id=store5, product_model=product5)
        
        # MassageChairModes
        mode1 = MassageChairModes.objects.create(massage_chair_mode_name='Mode One')
        mode2 = MassageChairModes.objects.create(massage_chair_mode_name='Mode Two')
        mode3 = MassageChairModes.objects.create(massage_chair_mode_name='Mode Three')
        mode4 = MassageChairModes.objects.create(massage_chair_mode_name='Mode Four')
        mode5 = MassageChairModes.objects.create(massage_chair_mode_name='Mode Five')
        
        # MassageChairRecord
        usage1 = MassageChairRecord.objects.create(customer=customer1, massage_chair=massage_chair1, massage_chair_mode=mode1, start_time=datetime.now(), payment='1')
        usage2 = MassageChairRecord.objects.create(customer=customer2, massage_chair=massage_chair2, massage_chair_mode=mode2, start_time=datetime.now(), payment='2')
        usage3 = MassageChairRecord.objects.create(customer=customer3, massage_chair=massage_chair3, massage_chair_mode=mode3, start_time=datetime.now(), payment='1')
        usage4 = MassageChairRecord.objects.create(customer=customer4, massage_chair=massage_chair4, massage_chair_mode=mode4, start_time=datetime.now(), payment='2')
        usage5 = MassageChairRecord.objects.create(customer=customer5, massage_chair=massage_chair5, massage_chair_mode=mode5, start_time=datetime.now(), payment='1')
        
        # SalesRecords
        sales_record1 = SalesRecords.objects.create(customer=customer1, product=product1, sales_time=datetime.now(), sales_type='1', salesperson=salesperson1, store=store1, sales_price=12000)
        sales_record2 = SalesRecords.objects.create(customer=customer2, product=product2, sales_time=datetime.now(), sales_type='2', salesperson=salesperson2, store=store2, sales_price=24000)
        sales_record3 = SalesRecords.objects.create(customer=customer3, product=product3, sales_time=datetime.now(), sales_type='1', salesperson=salesperson3, store=store3, sales_price=36000)
        sales_record4 = SalesRecords.objects.create(customer=customer4, product=product4, sales_time=datetime.now(), sales_type='2', salesperson=salesperson4, store=store4, sales_price=48000)
        sales_record5 = SalesRecords.objects.create(customer=customer5, product=product5, sales_time=datetime.now(), sales_type='1', salesperson=salesperson5, store=store5, sales_price=60000)
        
        # OnlineStoreVisits
        visit1 = OnlineStoreVisits.objects.create(customer=customer1, product=product2)
        visit2 = OnlineStoreVisits.objects.create(customer=customer2, product=product3)
        visit3 = OnlineStoreVisits.objects.create(customer=customer3, product=product4)
        visit4 = OnlineStoreVisits.objects.create(customer=customer4, product=product5)
        visit5 = OnlineStoreVisits.objects.create(customer=customer5, product=product1)
        
        # ReferralCodes
        referral_code1 = ReferralCodes.objects.create(customer=customer1, referral_code='abcdefg', used_referral_code='efghijk')
        referral_code2 = ReferralCodes.objects.create(customer=customer2, referral_code='hijklmn', used_referral_code='opqrstu')
        referral_code3 = ReferralCodes.objects.create(customer=customer3, referral_code='pqrstuv', used_referral_code='vwxyzab')
        referral_code4 = ReferralCodes.objects.create(customer=customer4, referral_code='yzabcd', used_referral_code='efghijk')
        referral_code5 = ReferralCodes.objects.create(customer=customer5, referral_code='efghijk', used_referral_code=None)
        
        # SalesQuestionnaires
        questionnaire1 = SalesQuestionnaires.objects.create(sales_record=sales_record1, sales_process_score=8, warranty_process_score=9)
        questionnaire2 = SalesQuestionnaires.objects.create(sales_record=sales_record2, sales_process_score=7, warranty_process_score=8)
        questionnaire3 = SalesQuestionnaires.objects.create(sales_record=sales_record3, sales_process_score=6, warranty_process_score=7)
        questionnaire4 = SalesQuestionnaires.objects.create(sales_record=sales_record4, sales_process_score=5, warranty_process_score=6)
        questionnaire5 = SalesQuestionnaires.objects.create(sales_record=sales_record5, sales_process_score=4, warranty_process_score=5)
        
        # ExperienceQuestionnaires
        experience1 = ExperienceQuestionnaires.objects.create(customer=customer1, usage_id=usage1, willingness_to_use_again=True, massage_chair_mode_satisfaction=8)
        experience2 = ExperienceQuestionnaires.objects.create(customer=customer2, usage_id=usage2, willingness_to_use_again=False, massage_chair_mode_satisfaction=7)
        experience3 = ExperienceQuestionnaires.objects.create(customer=customer3, usage_id=usage3, willingness_to_use_again=True, massage_chair_mode_satisfaction=6)
        experience4 = ExperienceQuestionnaires.objects.create(customer=customer4, usage_id=usage4, willingness_to_use_again=False, massage_chair_mode_satisfaction=5)
        experience5 = ExperienceQuestionnaires.objects.create(customer=customer5, usage_id=usage5, willingness_to_use_again=True, massage_chair_mode_satisfaction=4)
        
        # ExperienceReservations
        reservation1 = ExperienceReservations.objects.create(customer=customer1, reservation_time= current_time, store_id=store1, Salespeople=salesperson1)
        reservation2 = ExperienceReservations.objects.create(customer=customer2, reservation_time= current_time, store_id=store2, Salespeople=salesperson2)
        reservation3 = ExperienceReservations.objects.create(customer=customer3, reservation_time= current_time, store_id=store3, Salespeople=salesperson3)
        reservation4 = ExperienceReservations.objects.create(customer=customer4, reservation_time= current_time, store_id=store4, Salespeople=salesperson4)
        reservation5 = ExperienceReservations.objects.create(customer=customer5, reservation_time= current_time, store_id=store5, Salespeople=salesperson5)
        
    def test_models(self):
        self.assertEqual(len(Customers.objects.all()), 5)
        self.assertEqual(len(PhysicalStores.objects.all()), 5)
        self.assertEqual(len(Salespeople.objects.all()), 5)
        self.assertEqual(len(Products.objects.all()), 5)
        self.assertEqual(len(MassageChairs.objects.all()), 5)
        self.assertEqual(len(MassageChairModes.objects.all()), 5)
        self.assertEqual(len(MassageChairRecord.objects.all()), 5)
        self.assertEqual(len(SalesRecords.objects.all()), 5)
        self.assertEqual(len(OnlineStoreVisits.objects.all()), 5)
        self.assertEqual(len(ReferralCodes.objects.all()), 5)
        self.assertEqual(len(SalesQuestionnaires.objects.all()), 5)
        self.assertEqual(len(ExperienceQuestionnaires.objects.all()), 5)
        self.assertEqual(len(ExperienceReservations.objects.all()), 5)