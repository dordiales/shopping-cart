U
    )c�a�  �                   @   sr   d dl Zd dlm  mZ d dlT d dlmZ dd� Z	dd� Z
dd� Z
d	d
� Zdd� Zdd� Zdd� Zdd� ZdS )�    N)�*)�dedentc                  C   s�   t d�} dg}t| �}||k}|s�t�d|fd||f�dt�� ksLt�|�rVt�|�nddt�� ksnt�|�rxt�|�ndd� }dd	|i }tt�	|���d }d S )
Nz        pan|1|1.20
        �
pan|1|1.20��==�z%(py0)s == %(py2)s�expect�result�Zpy0Zpy2�assert %(py4)s�py4�
r   Zdividir_contenido�
@pytest_ar�_call_reprcompare�@py_builtins�locals�_should_repr_global_name�	_saferepr�AssertionError�_format_explanation��textr   r	   �@py_assert1�@py_format3�@py_format5� r   �S/home/penascal/trabajos/ainhoa-david-joseph-stephanie/back/test/test_placeholder.py�test_split_line   s    �  `   r   c                  C   s�   t d�} dddg}t| �}||k}|s�t�d|fd||f�dt�� ksPt�|�rZt�|�nddt�� ksrt�|�r|t�|�ndd	� }d
d|i }tt�	|���d }d S )NzF        pan|1|1.20
        queso|2|3.70
        Leche|12|0.84
        r   �queso|2|3.70�Leche|12|0.84r   r   r   r	   r
   r   r   r   r   r   r   r   �test_split_lines   s    �
  `   r    c                  C   s�   t d�} dg}t| �}||k}|s�t�d|fd||f�dt�� ksLt�|�rVt�|�nddt�� ksnt�|�rxt�|�ndd� }dd	|i }tt�	|���d }d S )
Nz+        carne de tochomosca|1|1.20
        zcarne de tochomosca|1|1.20r   r   r   r	   r
   r   r   r   r   r   r   r   r       s    �  `   c                  C   s�   dg} dddgg}t | �}||k}|s�t�d|fd||f�dt�� ksPt�|�rZt�|�nddt�� ksrt�|�r|t�|�ndd	� }d
d|i }tt�|���d }d S )Nr   �pan�1�1.20r   r   r   r	   r
   r   r   �	Zsepara_cada_elementor   r   r   r   r   r   r   r   r   r   r   r   �test_split_list_by_vertical_bar(   s      `   r%   c                  C   s�   dddg} dddgddd	gd
ddgg}t | �}||k}|s�t�d|fd||f�dt�� ksdt�|�rnt�|�nddt�� ks�t�|�r�t�|�ndd� }dd|i }tt�|���d }d S )Nr   r   r   r!   r"   r#   �queso�2�3.70�Leche�12�0.84r   r   r   r	   r
   r   r   r$   )�listr   r	   r   r   r   r   r   r   �!test_split_lists_by_vertical_bar_/   s    
  `   r-   c                  C   s�   dddd�} d}t | �}||k}|s�t�d|fd||f�dt�� ksNt�|�rXt�|�nddt�� kspt�|�rzt�|�ndd	� }d
d|i }tt�|���d }d S )Nr!   �   �333333�?)�product�cuantity�valuer   r   r   r	   r
   r   r   )	Zcalculated_subtotalr   r   r   r   r   r   r   r   )Zmydictr   r	   r   r   r   r   r   r   �test_if_subtotal_is_correct6   s      `   r3   c                  C   s�   dddgg} ddddd�g}t | �}||k}|s�t�d|fd||f�d	t�� ksZt�|�rdt�|�nd	d
t�� ks|t�|�r�t�|�nd
d� }dd|i }tt�|���d }d S )Nr!   r"   r#   r.   r/   �r0   r1   r2   Zsubtotalr   r   r   r	   r
   r   r   �	Zcrear_lista_de_diccionariosr   r   r   r   r   r   r   r   r   r   r   r   �test_list_as_dict=   s      `   r6   c                  C   s�   dddgdddgddd	gg} dd
ddd�ddddd�ddddd�g}t | �}||k}|s�t�d|fd||f�dt�� ks�t�|�r�t�|�nddt�� ks�t�|�r�t�|�ndd� }dd|i }tt�|���d }d S )Nr!   r"   r#   r&   r'   r(   r)   r*   r+   r.   r/   r4   �   g������@g������@�   g�z�G��?g)\���($@r   r   r   r	   r
   r   r   r5   r   r   r   r   �test_lists_as_dictD   s    �  `   r9   )�builtinsr   �_pytest.assertion.rewrite�	assertion�rewriter   Zsrc.main�textwrapr   r   r    r%   r-   r3   r6   r9   r   r   r   r   �<module>   s     