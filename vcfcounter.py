import vcf
import gzip

# Documentation for vcf is here: https://pyvcf.readthedocs.io/en/latest/index.html

vcf_reader = vcf.Reader(filename='data/ALL.chrY.phase3_integrated_v2b.20130502.genotypes.vcf.gz', compressed=True)

vcf_reader.fetch('Y')

records = 0

for record in vcf_reader:
    print(record)
    records += 1
    if records >= 20:
        break

print(f"We read {records} records in the vcf from the Y chromosome")
