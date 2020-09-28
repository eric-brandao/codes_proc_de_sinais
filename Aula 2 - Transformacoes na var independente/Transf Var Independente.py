#!/usr/bin/env python
# coding: utf-8

# # Transformações da variável independente
# 
# Neste notebook avaliaremos algumas transformações na variável independente. São elas:
# 
# 1. Deslocamento no tempo
# 2. Reflexão no tempo
# 3. Mudança de escala no tempo
# 
# Vamos analisar então uma por uma com alguns exemplos.

# In[2]:


# importar as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt


# ## 1. Deslocamento no tempo
# 
# Seja um sinal $x(t)$. O deslocamento no tempo é expresso por $x(t \pm t_0)$, sendo $t_0$ o deslocamento no tempo.
# 
# Para um $t_0$ positivo, $x(t-t_0)$ representa uma versão ***atrasada*** (ou deslocada para a ***direita***) de $x(t)$
# 
# Para um $t_0$ positivo, $x(t+t_0)$ representa uma versão ***adiantada*** (ou deslocada para a ***esquerda***) de $x(t)$
# 
# A mesma lógica se aplica a um sinal discreto $x[n]$. Para um $n_0$ inteiro e positivo, $x[n-n_0]$ representa uma versão ***atrasada*** (ou deslocada para a ***direita***) de $x[n]$. Para um $n_0$ inteiro e positivo, $x[n+n_0]$ representa uma versão ***adiantada*** (ou deslocada para a ***esquerda***) de $x[n]$.
# 
# Vamos trabalhar inicialmente em um sinal $x(t)$: a função sigmoide. Ela é muito conhecida em aprendizado de máquina e é definida por:
# 
# \begin{equation}
# x(t) = \frac{1}{1+\mathrm{e}^{-t}}
# \end{equation}

# In[93]:


# Sinal
t = np.linspace(-20, 20, 50) # vetor temporal
xt = 1/(1+np.exp(-t))

# Sinal deslocado
t_0 = -5 # deslocamento temporal
xt_des = 1/(1+np.exp(-(t-t_0)))

# Figura
plt.figure()
plt.title('Sinais original e deslocado')
plt.plot(t, xt, '-b', linewidth = 2, label = 'Original')
plt.plot(t, xt_des, '-r', linewidth = 2, label = 'Deslocado')
plt.legend(loc = 'best')
plt.grid(linestyle = '--', which='both')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [-]')
plt.tight_layout()
plt.show()

# Figura
plt.figure()
plt.title('Sinais original e deslocado')
plt.stem(t, xt_des, 'r',  label = r'$x[n-n_0]$', use_line_collection = True, basefmt=" ", markerfmt = 'C3o')
plt.stem(t, xt, 'b', label = r'$x[n]$', use_line_collection = True, basefmt=" ")

plt.legend(loc = 'best')
plt.grid(linestyle = '--', which='both')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [-]')
plt.tight_layout()
plt.show()


# ### O que se passa com uma função cossenoidal?
# 
# Se $x(t) = \mathrm{cos}(2  \pi f t) = \mathrm{cos}(\omega t)$,
# 
# O que $x(t-t_0)$ se torna?
# 
# Notamos que:
# 
# \begin{equation}
# x(t-t_0) = \mathrm{cos}(\omega (t-t_0)) = \mathrm{cos}(\omega t- \omega t_0)) 
# \end{equation}
# em que $\phi = \omega t_0$ é chamado de fase do sinal. Vamos olhar 3 aspectos dessa questão:
# 
# 1. Um deslocamento temporal é um deslocamento de fase. É uma questão semântica e frequentemente falamos de fase quando estamos trabalhando no domínio da frequência. A fase está relacionada com o "valor de início do meu cosseno".
# 
# 2. O que acontece quando deslocamos o cosseno de $\phi = \pi/2$?
# 
# 3. O que acontece quando damos um mesmo deslocamento temporal em duas frequências diferentes.
# 
# ![tri_circle.png](attachment:tri_circle.png)
# 

# In[44]:


# Sinal
t = np.linspace(-1, 1, 1000) # vetor temporal
freq = 1
w = 2*np.pi*freq
xt = np.cos(w*t)

# Sinal deslocado
t_0 = 0.1 # deslocamento temporal
phi = w*t_0 #np.pi/2
xt_des = np.cos(w*t - phi)

# Figura
plt.figure()
plt.title('Sinais original e deslocado')
plt.plot(t, xt, '-b', linewidth = 2, label = 'Original')
plt.plot(t, xt_des, '-r', linewidth = 2, label = 'Deslocado')
plt.legend(loc = 'best')
plt.grid(linestyle = '--', which='both')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [-]')
plt.tight_layout()
plt.show()


# ## 2. Reflexão no tempo
# 
# Seja um sinal $x(t)$. A reflexão no tempo é expressa por $x(-t)$. Isto é um espelhamento do sinal em torno do eixo $y$, ou seja, o sinal seria reproduzido ao contrário.
# 

# In[71]:


# Sinal
t = np.linspace(-20, 20, 1000) # vetor temporal
xt = 1/(1+np.exp(-t))

# Sinal refletido
xt_ref = np.flip(xt) # o método flip é usado para refletir o sinal

# Figura
plt.figure()
plt.title('Sinais original e refletido')
plt.plot(t, xt, '-b', linewidth = 2, label = 'Original')
plt.plot(t, xt_ref, '-r', linewidth = 2, label = 'Refletido')
plt.legend(loc = 'best')
plt.grid(linestyle = '--', which='both')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [-]')
plt.tight_layout()
plt.show()


# ## 3. Mudança de escala no tempo
# 
# Seja um sinal $x(t)$. A mudança de escala no tempo é expressa por $x(a  t)$, sendo $a>0$ um número positivo.
# 
# Se $0 < a < 1$, então $x(at)$ é uma versão ***alongada*** de $x(t)$ e, portanto, reproduzida com ***menor*** velocidade.
# 
# Se $a > 1$, então $x(at)$ é uma versão ***encurtada*** de $x(t)$ e, portanto, reproduzida com ***maior*** velocidade.

# In[73]:


# Sinal
t = np.linspace(-10, 10, 1000) # vetor temporal
xt = 1/(1+np.exp(-t))

# Sinal em outra escala
a = 2
xt_esc = 1/(1+np.exp(-a*t)) 

# Figura
plt.figure()
plt.title('Sinais original e refletido, with a = '+ str(a))
plt.plot(t, xt, '-b', linewidth = 2, label = 'Original')
plt.plot(t, xt_esc, '-r', linewidth = 2, label = 'Mud. de escala')
plt.legend(loc = 'best')
plt.grid(linestyle = '--', which='both')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [-]')
plt.tight_layout()
plt.show()


# ### O que se passa com uma função cossenoidal?
# 
# Se $x(t) = \mathrm{cos}(2  \pi f t) = \mathrm{cos}(\omega t)$,
# 
# $x(at)$ se torna um sinal com frequência diferente.

# In[64]:


# Sinal
t = np.linspace(0, 2, 1000) # vetor temporal
freq = 1
w = 2*np.pi*freq
xt = np.cos(w*t)

# Sinal com escala diferente
a = 2
xt_esc = np.cos(w*(a*t))

# Figura
plt.figure()
plt.title('Sinais original e com escala diferente')
plt.plot(t, xt, '-b', linewidth = 2, label = 'Original')
plt.plot(t, xt_esc, '-r', linewidth = 2, label = 'Mud. de escala')
plt.legend(loc = 'best')
plt.grid(linestyle = '--', which='both')
plt.xlabel('Tempo [s]')
plt.ylabel('Amplitude [-]')
plt.tight_layout()
plt.show()


# In[70]:


import sounddevice as sd
fs = 44100
t = np.linspace(0, 1, fs) # vetor temporal
freq = 1000
a = 1
w = 2*np.pi*freq
xt = np.sin(w*a*t)

sd.play(xt, fs)

