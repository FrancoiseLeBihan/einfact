#!/usr/bin/env python3
"""Claim-2 Table-1 check. Run only on the A100 configuration in README."""
import argparse, sys, pathlib
sys.path.insert(0,str(pathlib.Path(__file__).parent)); from common import *
def main():
 p=argparse.ArgumentParser(); add_common(p); p.set_defaults(iterations=200); a=p.parse_args()
 y,h=load(a,(27,7,24,100,100)); shapes=dict(w=27,h=7,d=24,i=100,j=100,r=10,k=24)
 # 10*(27+7+24+2*100*24)=48,580 exactly.
 custom='wr,hr,dr,ikr,jkr->whdij'; cp='wr,hr,dr,ir,jr->whdij'
 m1,z1=fit(y,h,custom,shapes,1.,1.,a)
 # CP rank 188 yields 48,504 parameters: closest capacity-matched integral rank.
 s2={**shapes,'r':188}; m2,z2=fit(y,h,cp,s2,1.,1.,a)
 v1=float(z1['heldout_loss'][-1]); v2=float(z2['heldout_loss'][-1])
 report(a,{'claim':2,'split':'provided' if a.heldout else 'hash-5%-NOT-paper-split','custom_parameters':48580,'cp_parameters':504*0+188*(27+7+24+100+100),'custom_heldout_mse':v1,'cp_heldout_mse':v2,'targets':{'custom':.0101,'cp':.0104},'pass':abs(v1-.0101)<=.0005 and abs(v2-.0104)<=.0005})
if __name__=='__main__': main()
