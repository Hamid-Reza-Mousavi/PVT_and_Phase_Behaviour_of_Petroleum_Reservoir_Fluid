# Property C6-C45
import pandas as pd
import numpy as np

def Tabel_Property():
    Mw = np.array([84, 96, 107, 121, 134, 147, 161, 175, 190, 206, 222, 237, 251, 263, 275, 291, 300, 312, 324, 337,
                   349, 360, 372, 382, 394, 404, 415, 426, 437, 445, 456, 464, 475, 484, 495, 502, 512, 521, 531, 539])
    property = pd.DataFrame({'MW': Mw}, index=[f'C{i}' for i in range(6, 46)])
    return property


def Table_Riazi_Daubert_SI():

    theta = np.array(['Tc', 'Tc', 'Pc', 'Pc', '(Vc/M)', '(Vc/M)',
                     'M', 'Tb'])
    theta1 = np.array(['Tb', 'M', 'Tb', 'M', 'Tb', 'M',
                     'Tb', 'M'])
    theta2 = np.array(['S', 'S', 'S', 'S', 'S', 'S',
                     'S', 'S'])
    a = np.array([9.5233, 3.08e2, 3.1958e4, 3.1166e2, 6.0490e-5,
                 7.5288e-4, 1.0321e3, 3.7659])
    b = np.array([-9.3140e-4, -1.3478e-4, -8.5050e-3, -1.8078e-3,
                 -2.6422e-3, -2.6570e-3, 9.7754e-4, 3.7741e-3])
    c = np.array([-0.54444, -0.61641, -4.8014, -0.3084, -0.26404,
                 0.5287, -9.53384, 2.984036])
    d = np.array([6.4791e-4, 0, 5.7490e-3, 0, 1.9710e-2, 2.6012e-3,
                 1.9990e-3, -4.2529e-3])
    e = np.array([0.81067, 0.2998, -0.4844, -0.8063, 0.7506,
                     0.20378, 0.97476, 0.401673])
    f = np.array([0.53691, 1.0555, 4.0846, 1.6015, -1.2028, -1.3036,
                  6.51274, -1.58262])
    Table_Riazi_Daubert = pd.DataFrame({'theta':theta, 'theta1':theta1, 'theta2':theta2,
                                  'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'f':f})
    return Table_Riazi_Daubert

def Table_Riazi_Daubert_Field():

    theta = np.array(['Tc', 'Tc', 'Pc', 'Pc', '(Vc/M)', '(Vc/M)',
                     'M', 'Tb'])
    theta1 = np.array(['Tb', 'M', 'Tb', 'M', 'Tb', 'M',
                     'Tb', 'M'])
    theta2 = np.array(['S', 'S', 'S', 'S', 'S', 'S',
                     'S', 'S'])
    a = np.array([10.6443, 544.4, 6.162e6, 4.5203e4,
                   6.233e-4, 1.206e-2, 581.96, 6.77857])
    b = np.array([-5.1747e-4, -1.3478e-4, -4.725e-3, -1.8078e-3,
                   -1.4679e-3, -2.657e-3, 5.43076e-4, 3.77409e-3])
    c = np.array([-0.54444, -0.61641, -4.8014, -0.3084,
                  -0.26404, 0.5278, -9.53384, 2.984036])
    d = np.array([3.5995e-4, 0, 3.1939e-3, 0,
                  1.095e-3, 2.6012e-3, 1.11056e-3, -4.25288e-3])
    e = np.array([0.81067, 0.2998, -0.4844, -0.8063,
                  0.7506, 0.20378, 0.97476, 0.401673])
    f = np.array([0.53691, 1.0555, 4.0846, 1.6015,
                  -1.2028, -1.3036, 6.51274, -1.58262])
    Table_Riazi_Daubert = pd.DataFrame({'theta':theta, 'theta1':theta1, 'theta2':theta2,
                                  'a':a, 'b':b, 'c':c, 'd':d, 'e':e, 'f':f})
    return Table_Riazi_Daubert