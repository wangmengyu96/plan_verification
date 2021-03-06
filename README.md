# RiskAssess
Code for:
Wang, Allen, et al. "Fast Risk Assessment for Autonomous Vehicles Using Learned Models of Agent Futures." arXiv preprint arXiv:2005.13458 (2020).

We are currently in the process of organizing and cleaning up our code for presentation to the public. 

## Setup
Run `source setup.sh`. It will create a virtual environment that allows you to run the code, so you just need to run `source venv/bin/activate` and you should be able to run things.

## Examples
`/examples/position_risk_assessment.py` utilizes the GMM position risk assessment methods.

**STILL CLEANING UP**: `/examples/control_risk_assessment` utilizes the control risk assessment methods. TreeRing is included in a separate package [AlgebraicMoments](https://github.com/allen-adastra/algebraic_moments).


All code for SOS risk assessment is in `/risk_assess/sos_risk_assessment`. We use Yalmip, so the SOS code is in MATLAB.

## Contact
Allen Wang, allenw@mit.edu

Cyrus Huang, xhuang@csail.mit.edu
