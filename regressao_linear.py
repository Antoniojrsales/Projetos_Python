{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "f3abb9ad-02e2-46e2-bd45-2ee68b17275d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "============Contagem Lista X============\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Digite os valores de x:  1\n",
      "Digite os valores de x:  2\n",
      "Digite os valores de x:  3\n",
      "Digite os valores de x:  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "============Contagem Lista Y============\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Digite os valores de y:  3\n",
      "Digite os valores de y:  5\n",
      "Digite os valores de y:  6\n",
      "Digite os valores de y:  8\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "===============RESULTADO================\n",
      "O resultado de Beta1 e 1.6\n",
      "O resultado de Beta0 e 1.5\n",
      "========================================\n"
     ]
    }
   ],
   "source": [
    "print('{:=^40}'.format('Contagem Lista X'))\n",
    "lista_x = []\n",
    "lista_y = []\n",
    "for listas_x in range(0, 4):\n",
    "    listas_x = int(input('Digite os valores de x: '))\n",
    "    lista_x.append(listas_x)\n",
    "    soma_x = sum(lista_x)    \n",
    "print('{:=^40}'.format('Contagem Lista Y'))\n",
    "for listas_y in range(0, 4):\n",
    "    listas_y = int(input('Digite os valores de y: '))\n",
    "    lista_y.append(listas_y)\n",
    "    soma_y = sum(lista_y)\n",
    "    xy = [ (a * b) for a, b in zip(lista_x, lista_y) ]\n",
    "    soma_xy = sum(xy)\n",
    "    soma_x2 = lista_x[0] ** 2 + lista_x[1] ** 2 + lista_x[2] ** 2 + lista_x[3] ** 2\n",
    "beta_zero = (soma_x * soma_xy - soma_y * soma_x2) / (soma_x ** 2 - 4 * soma_x2)\n",
    "beta_um = (4 * soma_xy - soma_x * soma_y) / (4 * soma_x2 - soma_x ** 2)\n",
    "print('{:=^40}'.format('RESULTADO'))\n",
    "print(f'O resultado de Beta1 e {beta_um}')\n",
    "print(f'O resultado de Beta0 e {beta_zero}')\n",
    "print('='*40)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "cf582260-4314-435d-887a-a88bfbbb2204",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "22"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "soma_y"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
