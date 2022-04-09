# bp=buy price per share
# bpno=No of share bought
# total_bp=total buy price

# sp=sell price per share
# spno=No of share sold
# total_sp=total sell price

# val=Change

def profit(sp,bp,val,total_bp,total_sp):
    print("\nIts a profit!")
    print("Profit per share=",sp-bp,"Rupees")
    print("Total profit=",total_sp-total_bp,"Rupees")
    print("Profit in %",(val*100)/total_bp,"%")
    print("Profit ratio",(total_sp/total_bp))
    print("For every one rupee, you gained",total_sp/total_bp,"Rupees\n")

def loss(sp,bp,val,total_bp,total_sp):
    print("\nIts a loss!")
    print("Loss per share=",sp-bp,"Rupees")
    print("Total loss=",total_sp-total_bp,"Rupees")
    print("Loss in %",(val*100)/total_bp,"%")
    print("Loss ratio",(total_sp/total_bp))
    print("For every one rupee, you lost",total_sp/total_bp,"Rupees\n")

def null(total_bp,total_sp):
    print("\nIts a break-even!")
    print("You have made 0 profit and 0 loss")
    print("For every one rupee, you lost",total_bp/total_sp,"Rupees\n")

print("\nWelcome to share market calculator")

bp=float(input("Enter buying price:"))
bpno=int(input("Enter the number of share:"))
total_bp=bp*bpno
print("Total BP=",total_bp)

sp=float(input("\nEnter the sell price:"))
spno=int(input("Enter the number of share:"))
total_sp=sp*spno
print("Toral SP=",total_sp)

val=total_sp-total_bp

if val>0:
    profit(sp,bp,val,total_bp,total_sp)
elif val==0:
    null(total_bp,total_sp)
else:
    loss(sp,bp,val,total_bp,total_sp)
