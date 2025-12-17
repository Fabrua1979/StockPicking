import React from "react";
import { RegisterSlide } from "@/decorators/RegisterSlide";

const Slide02Overview: React.FC = () => {
  return (
    <section className="flex h-full flex-col px-16 py-12 bg-gradient-to-br from-slate-900 to-black">
      <h1 className="text-5xl font-bold text-blue-400 mb-8">Panoramica del Sistema</h1>
      
      <div className="flex-1 min-h-0 grid grid-cols-2 gap-8">
        {/* Left Column - Strategy Cards */}
        <div className="flex flex-col gap-4">
          <div className="bg-emerald-500/10 border border-emerald-500/30 rounded-xl p-6">
            <div className="flex items-center gap-3 mb-3">
              <span className="text-4xl">🛡️</span>
              <h3 className="text-2xl font-semibold text-emerald-300">Strategia Conservativa</h3>
            </div>
            <p className="text-slate-300 text-base">
              Vendita di Put OTM (Out-of-The-Money) con delta -0.05/-0.10, protezioni automatiche e gestione margine dinamica.
            </p>
          </div>

          <div className="bg-amber-500/10 border border-amber-500/30 rounded-xl p-6">
            <div className="flex items-center gap-3 mb-3">
              <span className="text-4xl">⚡</span>
              <h3 className="text-2xl font-semibold text-amber-300">Strategia Semi-Conservativa</h3>
            </div>
            <p className="text-slate-300 text-base">
              Vendita di Put con strike più vicini (delta -0.01/-0.08), rendimenti maggiori con rischio controllato e sistema di alert avanzato.
            </p>
          </div>

          <div className="bg-violet-500/10 border border-violet-500/30 rounded-xl p-6">
            <div className="flex items-center gap-3 mb-3">
              <span className="text-4xl">🌊</span>
              <h3 className="text-2xl font-semibold text-violet-300">Strategia SCV (Opzionale)</h3>
            </div>
            <p className="text-slate-300 text-base">
              Sell Call Volatility su VIX - Profitto dalla discesa della volatilità dopo spike improvvisi. Attivabile a scelta dell'utente.
            </p>
          </div>
        </div>

        {/* Right Column - Key Features */}
        <div className="flex flex-col gap-4">
          <div className="bg-slate-800/50 border border-slate-700 rounded-xl p-6 flex-1">
            <h3 className="text-2xl font-semibold text-white mb-4">🎯 Caratteristiche Principali</h3>
            <ul className="space-y-3 text-slate-300 text-base">
              <li className="flex items-start gap-3">
                <span className="text-blue-400 text-xl">✓</span>
                <span>Gestione automatica del rischio con margine dinamico</span>
              </li>
              <li className="flex items-start gap-3">
                <span className="text-blue-400 text-xl">✓</span>
                <span>Sistema alert a 2 soglie (50%, 75%)</span>
              </li>
              <li className="flex items-start gap-3">
                <span className="text-blue-400 text-xl">✓</span>
                <span>Coperture automatiche su eventi "Cigno Nero"</span>
              </li>
              <li className="flex items-start gap-3">
                <span className="text-blue-400 text-xl">✓</span>
                <span>Monitoraggio real-time con dashboard completa</span>
              </li>
              <li className="flex items-start gap-3">
                <span className="text-blue-400 text-xl">✓</span>
                <span>4 profili di ingresso configurabili</span>
              </li>
              <li className="flex items-start gap-3">
                <span className="text-blue-400 text-xl">✓</span>
                <span>Configurazioni ottimizzate per 5 broker diversi</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>
  );
};

RegisterSlide({
  title: "Panoramica del Sistema",
  order: 1,
})(Slide02Overview);

export default Slide02Overview;