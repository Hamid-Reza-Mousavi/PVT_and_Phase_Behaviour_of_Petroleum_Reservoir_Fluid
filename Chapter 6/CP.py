import pandas as pd
import numpy as np

class CriticalProperties():
    def __init__(self, Unit='SI'):
        self.Unit = Unit
    def Lee_Kesler(self, Tb, S, omega_method='Lee-Kesler', Pb=0.1013):
        self.Tb = Tb
        self.S = S
        self.omega_method = omega_method
        self.Pb = Pb
        
        if self.Unit == 'SI':   
            self.Tc = 189.8 + 450.6*self.S + (0.4244+0.1174*self.S)*self.Tb+ \
                (0.1441-1.0069*self.S) * 1e5 / self.Tb
            
            self.Pc = np.exp(3.3864 - 0.0566/self.S - (0.43639+4.1216/self.S+ \
                0.21343/self.S**2) * 1e-3*self.Tb + (0.47579+1.182/self.S+ \
                0.15302/self.S**2) * 1e-6*self.Tb**2 - (2.4505+9.9099/self.S**2) * \
                1e-10*self.Tb**3)
            
            self.Tbr = self.Tb/self.Tc
            self.Pbr = self.Pb/self.Pc
            self.Kw = (1.8*self.Tb)**(1/3) / self.S
            if self.omega_method == 'Lee-Kesler':
                
                if  self.Tbr <= 0.8:
                    self.omega = ( np.log(self.Pbr)-5.92714+6.09648/self.Tbr+1.28862*np.log(self.Tbr) - \
                                 -0.16934*self.Tbr**6 ) / ( 15.2518-15.6875/self.Tbr-13.4721*np.log(self.Tbr)+ \
                                 0.43577*self.Tbr**6 )
                else:
                    self.omega = -7.904 + 0.1352*self.Kw - 0.007465*self.Kw**2 + 8.359*self.Tbr + \
                        (1.408-0.01064*self.Kw)/self.Tbr
            if self.omega_method == 'Edmister':
                self.Pa = 0.1013
                self.omega = ( (3/7)*np.log10(self.Pc/self.Pa) / ((self.Tc/self.Tb)-1) ) - 1
            
            self.Zc = 0.2901 - 0.0879 * self.omega
            
        elif self.Unit == 'Field':
            self.Tc = 341.7 + 811*self.S + (0.4244+0.1174*self.S)*self.Tb+ \
                (0.4669-3.2923*self.S) * 1e5 / self.Tb
            
            self.Pc = np.exp(8.3634-0.0566/self.S - (0.24244+2.2898/self.S+ \
                0.11857/self.S**2) * 1e-3*self.Tb + (1.4685+3.648/self.S+ \
                0.47227/self.S**2) * 1e-6*self.Tb**2 - (0.42019+1.6977/self.S**2) * \
                1e-10*self.Tb**3)
            
            self.Tbr = self.Tb/self.Tc
            self.Pbr = self.Pb/self.Pc
            self.Kw = (1.8*self.Tb)**(1/3) / self.S
            if self.omega_method == 'Lee-Kesler':
                
                if  self.Tbr <= 0.8:
                    self.omega = ( np.log(self.Pbr)-5.92714+6.09648/self.Tbr+1.28862*np.log(self.Tbr) - \
                                 -0.16934*self.Tbr**6 ) / ( 15.2518-15.6875/self.Tbr-13.4721*np.log(self.Tbr)+ \
                                 0.43577*self.Tbr**6 )
                else:
                    self.omega = -7.904 + 0.1352*self.Kw - 0.007465*self.Kw**2 + 8.359*self.Tbr + \
                        (1.408-0.01064*self.Kw)/self.Tbr
            if self.omega_method == 'Edmister':
                self.Pa = 0.1013
                self.omega = ( (3/7)*np.log10(self.Pc/self.Pa) / ((self.Tc/self.Tb)-1) ) - 1
            
            self.Zc = 0.2901 - 0.0879 * self.omega
            
    def Riazi_Daubert(self, theta1, theta2, Tabel, Tabel_index_selection=0):
        self.Tabel = Tabel
        self.Tabel_index_selection = Tabel_index_selection
        self.RD_a = self.Tabel.iloc[self.Tabel_index_selection]['a']
        self.RD_b = self.Tabel.iloc[self.Tabel_index_selection]['b']
        self.RD_c = self.Tabel.iloc[self.Tabel_index_selection]['c']
        self.RD_d = self.Tabel.iloc[self.Tabel_index_selection]['d']
        self.RD_e = self.Tabel.iloc[self.Tabel_index_selection]['e']
        self.RD_f = self.Tabel.iloc[self.Tabel_index_selection]['f']
        self.theta_name = self.Tabel.iloc[self.Tabel_index_selection]['theta']
        self.theta1_name = self.Tabel.iloc[self.Tabel_index_selection]['theta1']
        self.theta2_name = self.Tabel.iloc[self.Tabel_index_selection]['theta2']
        self.theta1 = theta1
        self.theta2 = theta2

        self.theta = self.RD_a * (np.exp(self.RD_b*self.theta1+self.RD_c*self.theta2+ \
            self.RD_d*self.theta1*self.theta2)) * self.theta1**self.RD_e * self.theta2**self.RD_f