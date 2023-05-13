#!/usr/bin/env python
# coding: utf-8
import tkinter as tk
from math import sqrt

class SpecialRelativity:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x400")
        self.root.title("Special Relativity Calculator")
        
        text = "A stationary observer on Earth sees a rocket traveling at a speed of v from the Earth to Alpha Centauri which is 4.367 light years away from the Earth."
        self.label = tk.Label(self.root, text=text, wraplength=400)
        self.label.pack(padx=10, pady=10)
        
        self.speed = tk.DoubleVar()
        self.speed.set(0.00)
        self.trip_duration = tk.IntVar()
        self.trip_duration.set(0)
        self.gamma_factor = tk.DoubleVar()
        self.time_on_rocket = tk.DoubleVar()
        self.length_contraction = tk.DoubleVar()
        
        self.speed_slider = tk.Scale(self.root, from_=0.00, to=0.99, resolution=0.01, length=300, orient=tk.HORIZONTAL, label="Speed (C)", variable=self.speed, command=self.calculate)
        self.speed_slider.pack()
        
        self.trip_duration_slider = tk.Scale(self.root, from_=0, to=20, resolution=1, length=300, orient=tk.HORIZONTAL, label="Trip Duration as Measured by the Earth (years)", variable=self.trip_duration, command=self.calculate)
        self.trip_duration_slider.pack()
        
        self.gamma_factor_label = tk.Label(self.root, textvariable=self.gamma_factor)
        self.gamma_factor_label.pack()
        
        self.time_on_rocket_label = tk.Label(self.root, textvariable=self.time_on_rocket)
        self.time_on_rocket_label.pack()
        
        self.length_contraction_label = tk.Label(self.root, textvariable=self.length_contraction)
        self.length_contraction_label.pack()
        
        self.calculate()
        
        self.root.mainloop()
        
    def calculate(self, *args):
        c = 1.0 # speed of light
        v = self.speed.get() * c # velocity as a fraction of c
        gamma_factor = 1 / sqrt(1 - v**2)
        self.gamma_factor.set(f"Gamma Factor: {gamma_factor:.2f}")
        
        trip_duration_earth = self.trip_duration.get()
        time_on_rocket = trip_duration_earth / gamma_factor
        self.time_on_rocket.set(f"Trip Duration as Measured by the Rocket: {time_on_rocket:.2f} years")
        
        length_contraction = 4.367 / gamma_factor
        self.length_contraction.set(f"Distance between Earth and Alpha Centaury According to the Rocket: {length_contraction:.2f} light years")
        
if __name__ == "__main__":
    SpecialRelativity()

