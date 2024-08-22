function F = F_cal(M, tau, gamma, Beta)

    F = ((M - tau)^(gamma - 1) * exp(-(M - tau) / Beta)) / (Beta^gamma * G(gamma));
    
end
