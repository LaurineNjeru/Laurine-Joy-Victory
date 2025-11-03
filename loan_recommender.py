#loan recommender
print("\n=== AI-BASED LOAN RECOMMENDER SYSTEM===")
print("-----------------------------------------")
#input details
name=input("enter the applicant name:")
fuliza_limit=float(input("enter the fuliza limit:"))
monthly_salary=float(input("enter the monthly salary:"))
crb_status=str(input("enter the crb status(listed/not listed):"))
#validation
if fuliza_limit/monthly_salary<0:
    print("error.Fuliza limit can't be negative")
    exit()
#Loan Recommendation Criteria
if fuliza_limit>10000 and monthly_salary>50000:
        crb_status="not listed"
        Loan_category="platinum loan"
        maximumloan_limit="1,000,000"
        remarks="Excellent Borrower"
elif 5000<= fuliza_limit <=10000 and 30000 <= monthly_salary <=50000:
        crb_status="not listed"
        Loan_category="gold loan"
        maximumloan_limit="500,000"
        remarks="Reliable Borrower"
elif fuliza_limit <5000 and monthly_salary <30000:
        crb_status="not listed"
        Loan_category="silver loan"
        maximumloan_limit="100,000"
        remarks="Fair Borrower"
else:
        crb_status="listed"
        Loan_category="not eligible"
        maximumloan_limit="0"
        remarks="crb issues detected"

#display results
print("\n=== AI-BASED LOAN RECOMMENDER SYSTEM===")
print("Name:",name)
print("Fuliza Limit:",fuliza_limit)
print("MONTHLY Salary:",monthly_salary)
print("CRB Status:",crb_status)
print("Loan Category:",Loan_category)
print("Maximum Loan Limit:",maximumloan_limit)
print("Remarks :",remarks)

print("\nError: invalid Monthly salary and fuliza limit. We regret to inform you that you ain't eligible for a loan.Borrow Your Friends😒")
exit()
