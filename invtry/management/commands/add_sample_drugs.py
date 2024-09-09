from django.core.management.base import BaseCommand
from invtry.models import Drug

class Command(BaseCommand):
    help = 'Populate the database with 30 sample drugs'

    def handle(self, *args, **kwargs):
        drugs = [
            {'drugid': '001', 'name': 'Aspirin', 'manufacturer': 'Bayer', 'drugtype': 'Tablet', 'quantity': 100, 'expirydate': '2025-12-01', 'description': 'Pain reliever', 'batchno': 'AB12345'},
            {'drugid': '002', 'name': 'Paracetamol', 'manufacturer': 'ABC Pharma', 'drugtype': 'Tablet', 'quantity': 200, 'expirydate': '2025-06-30', 'description': 'Fever reducer', 'batchno': 'BC45678'},
            {'drugid': '003', 'name': 'Ibuprofen', 'manufacturer': 'Pfizer', 'drugtype': 'Tablet', 'quantity': 150, 'expirydate': '2024-11-15', 'description': 'Anti-inflammatory', 'batchno': 'CD78901'},
            {'drugid': '004', 'name': 'Amoxicillin', 'manufacturer': 'GSK', 'drugtype': 'Capsule', 'quantity': 180, 'expirydate': '2025-08-20', 'description': 'Antibiotic', 'batchno': 'DE01234'},
            {'drugid': '005', 'name': 'Metformin', 'manufacturer': 'Merck', 'drugtype': 'Tablet', 'quantity': 220, 'expirydate': '2024-05-10', 'description': 'Diabetes management', 'batchno': 'EF34567'},
            {'drugid': '006', 'name': 'Lisinopril', 'manufacturer': 'Novartis', 'drugtype': 'Tablet', 'quantity': 140, 'expirydate': '2025-01-25', 'description': 'Blood pressure', 'batchno': 'FG67890'},
            {'drugid': '007', 'name': 'Simvastatin', 'manufacturer': 'AstraZeneca', 'drugtype': 'Tablet', 'quantity': 160, 'expirydate': '2024-07-18', 'description': 'Cholesterol control', 'batchno': 'GH12345'},
            {'drugid': '008', 'name': 'Omeprazole', 'manufacturer': 'Johnson & Johnson', 'drugtype': 'Capsule', 'quantity': 130, 'expirydate': '2025-09-22', 'description': 'Acid reflux', 'batchno': 'IJ45678'},
            {'drugid': '009', 'name': 'Citalopram', 'manufacturer': 'Eli Lilly', 'drugtype': 'Tablet', 'quantity': 170, 'expirydate': '2024-12-05', 'description': 'Antidepressant', 'batchno': 'JK78901'},
            {'drugid': '010', 'name': 'Gabapentin', 'manufacturer': 'Pfizer', 'drugtype': 'Tablet', 'quantity': 190, 'expirydate': '2025-03-16', 'description': 'Neuropathic pain', 'batchno': 'LM01234'},
            {'drugid': '011', 'name': 'Azithromycin', 'manufacturer': 'Zydus', 'drugtype': 'Tablet', 'quantity': 210, 'expirydate': '2024-10-29', 'description': 'Antibiotic', 'batchno': 'MN34567'},
            {'drugid': '012', 'name': 'Hydrochlorothiazide', 'manufacturer': 'Roche', 'drugtype': 'Tablet', 'quantity': 150, 'expirydate': '2025-02-15', 'description': 'Diuretic', 'batchno': 'OP67890'},
            {'drugid': '013', 'name': 'Clopidogrel', 'manufacturer': 'Boehringer Ingelheim', 'drugtype': 'Tablet', 'quantity': 180, 'expirydate': '2024-11-20', 'description': 'Antiplatelet', 'batchno': 'QR12345'},
            {'drugid': '014', 'name': 'Furosemide', 'manufacturer': 'Sandoz', 'drugtype': 'Tablet', 'quantity': 170, 'expirydate': '2025-06-05', 'description': 'Diuretic', 'batchno': 'ST45678'},
            {'drugid': '015', 'name': 'Levothyroxine', 'manufacturer': 'Mylan', 'drugtype': 'Tablet', 'quantity': 200, 'expirydate': '2024-09-10', 'description': 'Thyroid hormone', 'batchno': 'UV78901'},
            {'drugid': '016', 'name': 'Prednisone', 'manufacturer': 'Teva', 'drugtype': 'Tablet', 'quantity': 160, 'expirydate': '2025-05-15', 'description': 'Corticosteroid', 'batchno': 'WX01234'},
            {'drugid': '017', 'name': 'Sertraline', 'manufacturer': 'GlaxoSmithKline', 'drugtype': 'Tablet', 'quantity': 150, 'expirydate': '2024-12-01', 'description': 'Antidepressant', 'batchno': 'YZ34567'},
            {'drugid': '018', 'name': 'Doxycycline', 'manufacturer': 'Cipla', 'drugtype': 'Capsule', 'quantity': 140, 'expirydate': '2025-04-20', 'description': 'Antibiotic', 'batchno': 'AB67890'},
            {'drugid': '019', 'name': 'Lorazepam', 'manufacturer': 'Sun Pharma', 'drugtype': 'Tablet', 'quantity': 130, 'expirydate': '2024-07-10', 'description': 'Anxiolytic', 'batchno': 'CD90123'},
            {'drugid': '020', 'name': 'Allopurinol', 'manufacturer': 'Bristol-Myers Squibb', 'drugtype': 'Tablet', 'quantity': 160, 'expirydate': '2025-01-18', 'description': 'Gout management', 'batchno': 'EF23456'},
            {'drugid': '021', 'name': 'Methylprednisolone', 'manufacturer': 'Sandoz', 'drugtype': 'Tablet', 'quantity': 170, 'expirydate': '2024-10-30', 'description': 'Anti-inflammatory', 'batchno': 'GH34567'},
            {'drugid': '022', 'name': 'Naproxen', 'manufacturer': 'Apotex', 'drugtype': 'Tablet', 'quantity': 150, 'expirydate': '2025-03-22', 'description': 'Pain reliever', 'batchno': 'IJ45678'},
            {'drugid': '023', 'name': 'Ranitidine', 'manufacturer': 'Boehringer Ingelheim', 'drugtype': 'Tablet', 'quantity': 200, 'expirydate': '2024-12-20', 'description': 'Acid reducer', 'batchno': 'KL56789'},
            {'drugid': '024', 'name': 'Digoxin', 'manufacturer': 'Merck', 'drugtype': 'Tablet', 'quantity': 180, 'expirydate': '2025-07-15', 'description': 'Heart medication', 'batchno': 'MN67890'},
            {'drugid': '025', 'name': 'Tamsulosin', 'manufacturer': 'Eli Lilly', 'drugtype': 'Capsule', 'quantity': 170, 'expirydate': '2024-08-10', 'description': 'Benign prostatic hyperplasia', 'batchno': 'OP12345'},
            {'drugid': '026', 'name': 'Cetirizine', 'manufacturer': 'GlaxoSmithKline', 'drugtype': 'Tablet', 'quantity': 150, 'expirydate': '2025-11-05', 'description': 'Allergy relief', 'batchno': 'QR45678'},
            {'drugid': '027', 'name': 'Duloxetine', 'manufacturer': 'Pfizer', 'drugtype': 'Capsule', 'quantity': 160, 'expirydate': '2024-09-15', 'description': 'Antidepressant', 'batchno': 'ST78901'},
            {'drugid': '028', 'name': 'Ezetimibe', 'manufacturer': 'AstraZeneca', 'drugtype': 'Tablet', 'quantity': 140, 'expirydate': '2025-05-25', 'description': 'Cholesterol control', 'batchno': 'UV01234'},
            {'drugid': '029', 'name': 'Fluticasone', 'manufacturer': 'GSK', 'drugtype': 'Inhaler', 'quantity': 130, 'expirydate': '2024-06-30', 'description': 'Asthma management', 'batchno': 'WX34567'},
            {'drugid': '030', 'name': 'Propranolol', 'manufacturer': 'Bayer', 'drugtype': 'Tablet', 'quantity': 180, 'expirydate': '2025-10-20', 'description': 'Beta-blocker', 'batchno': 'YZ67890'},
        ]

        # Save drugs to database
        for drug in drugs:
            Drug.objects.create(**drug)

        self.stdout.write(self.style.SUCCESS('Successfully populated 30 drugs'))
