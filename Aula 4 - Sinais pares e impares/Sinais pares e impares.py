#!/usr/bin/env python
# coding: utf-8

# # Sinais pares (even) e ímpares (odd)
# 
# Neste notebook avaliaremos o que são sinais pares (even) e ímpares (odd) e como decompor um sinal que não é par ou ímpar em suas partes par e ímpar. Esta propriedade dos sinais está ligada a ***reflexão no tempo***, uma transformação da variável independente.
# 
# ## Sinal par (even)
# 
# Um sinal é dito ter simetria par se:
# 
# \begin{equation}
# x(-t) = x(t)
# \end{equation}
# 
# ou no caso de um sinal discreto
# 
# \begin{equation}
# x[-n] = x[n]
# \end{equation}
# 
# 
# ## Sinal ímpar (odd)
# 
# Um sinal é dito ter simetria ímpar se:
# 
# \begin{equation}
# x(-t) = -x(t)
# \end{equation}
# 
# ou no caso de um sinal discreto
# 
# \begin{equation}
# x[-n] = -x[n]
# \end{equation}
# o que implica que $x(0) = 0$ e  $x[0] = 0$.
# 
# Se temos um sinal $x(t)$ que não é par ou ímpar, é possível decompor tal sinal em: um sinal par e um sinal ímpar. As partes par (even) e ímpar (odd) são dadas por: 
# 
# \begin{equation}
# \epsilon v\left\{x(t)\right\}= \frac{1}{2}\left[x(t) + x(-t)\right]
# \end{equation}
# 
# \begin{equation}
# \mathcal{O}d\left\{x(t)\right\}= \frac{1}{2}\left[x(t) - x(-t)\right]
# \end{equation}
# 

# In[9]:


# importar as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt


# # Exemplos de sinais pares
# 
# 1. A função sigmoide
# 
# \begin{equation}
# x_1(t) = \frac{1}{1+\mathrm{e}^{-t}}
# \end{equation}
# 
# 2. A função cosseno
# 
# \begin{equation}
# x_2(t) = \mathrm{cos}(2 \pi f t)
# \end{equation}

# In[20]:


t = np.linspace(-5, 5, 1000) # vetor temporal

# Sigmoide
x1t = 1/(1+np.exp(-t))

# Cosseno
x2t = np.cos(2*np.pi*0.25*t)


# Figura
plt.figure()
plt.title('Sinal par')
plt.plot(t, x1t, '-b', linewidth = 2)
plt.grid(linestyle = '--', which='both')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [-]')
plt.tight_layout()
plt.show()

# Figura
plt.figure()
plt.title('Sinal par')
plt.plot(t, x2t, '-b', linewidth = 2)
plt.grid(linestyle = '--', which='both')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [-]')
plt.tight_layout()
plt.show()


# # Exemplos de sinais ímpares
# 
# 1. A exponencial do módulo
# 
# \begin{equation}
# x_1(t) = \mathrm{e}^{-|t|}
# \end{equation}
# 
# 2. A função seno
# 
# \begin{equation}
# x_2(t) = \mathrm{sin}(2 \pi f t)
# \end{equation}

# In[21]:


t = np.linspace(-5, 5, 1000) # vetor temporal

# Exp do módulo
x1t = np.exp(-np.abs(t))

# Seno
x2t = np.sin(2*np.pi*0.25*t)


# Figura
plt.figure()
plt.title('Sinal par')
plt.plot(t, x1t, '-r', linewidth = 2)
plt.grid(linestyle = '--', which='both')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [-]')
plt.tight_layout()
plt.show()

# Figura
plt.figure()
plt.title('Sinal par')
plt.plot(t, x2t, '-r', linewidth = 2)
plt.grid(linestyle = '--', which='both')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [-]')
plt.tight_layout()
plt.show()


# # Decomposição do sinal nas partes par e ímpar

# In[29]:


t = np.linspace(-1, 1, 20) # vetor temporal
xt = np.random.randn(len(t)) # Um sinal aleatório

# parte par
xt_ev = 0.5*(xt + np.flip(xt))

# parte par
xt_odd = 0.5*(xt - np.flip(xt))

# Figura
plt.figure()
plt.title('Sinal nem par nem ímpar')
plt.plot(t, xt, '-k', linewidth = 2)
plt.grid(linestyle = '--', which='both')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [-]')
plt.tight_layout()
plt.show()

plt.figure()
plt.subplot(2,1,1)
plt.title('Parte par')
plt.plot(t, xt_ev, '-b', linewidth = 2)
plt.grid(linestyle = '--', which='both')
plt.ylabel('Amplitude [-]')


plt.subplot(2,1,2)
plt.title('Parte ímpar')
plt.plot(t, xt_odd, '-r', linewidth = 2)
plt.grid(linestyle = '--', which='both')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [-]')
plt.tight_layout()
plt.show()

