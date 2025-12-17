import React from "react";
import { RegisterSlide } from "@/decorators/RegisterSlide";

const Slide09Dashboard: React.FC = () => {
  return (
    <section className="flex h-full flex-col px-16 py-10 bg-gradient-to-br from-slate-900 to-black">
      <h1 className="text-5xl font-bold text-cyan-400 mb-6">Dashboard e Monitoraggio</h1>
      
      <div className="flex-1 min-h-0 grid grid-cols-2 gap-6">
        {/* Left Column - Dashboard Features */}
        <div className="flex flex-col gap-3">
          <div className="bg-cyan-500/10 border border-cyan-500/30 rounded-xl p-4">
            <h3 className="text-lg font-semibold text-cyan-300 mb-2">📊 Stato Attivo (Bottom Left)</h3>
            <p className="text-slate-300 text-xs mb-2">Informazioni posizioni aperte in tempo reale:</p>
            <ul className="space-y-1 text-slate-400 text-xs">
              <li>• Strike, contratti, premio incassato</li>
              <li>• Giorni alla scadenza (DTE)</li>
              <li>• P/L in tempo reale</li>
              <li>• Occupazione margine dinamica (%)</li>
            </ul>
          </div>

          <div className="bg-slate-800/50 border border-slate-700 rounded-xl p-4">
            <h3 className="text-lg font-semibold text-white mb-2">⚡ Eventi Istantanei</h3>
            <p className="text-slate-300 text-xs mb-2">Notifiche su barra corrente:</p>
            <ul className="space-y-1 text-slate-400 text-xs">
              <li>• Aperture/chiusure posizioni</li>
              <li>• Attivazione coperture</li>
              <li>• Alert margine S1/S2</li>
              <li>• Rifinanziamenti e prelievi</li>
            </ul>
          </div>

          <div className="bg-slate-800/50 border border-slate-700 rounded-xl p-4">
            <h3 className="text-lg font-semibold text-white mb-2">📖 Book Opzioni Live</h3>
            <p className="text-slate-300 text-xs mb-2">Prezzi real-time per ogni strike:</p>
            <ul className="space-y-1 text-slate-400 text-xs">
              <li>• PUT Buy / PUT Sell</li>
              <li>• CALL Buy / CALL Sell</li>
              <li>• Aggiornamento continuo</li>
            </ul>
          </div>
        </div>

        {/* Right Column - Tables and Stats */}
        <div className="flex flex-col gap-3">
          <div className="bg-slate-800/50 border border-slate-700 rounded-xl p-4">
            <h3 className="text-lg font-semibold text-emerald-300 mb-2">📈 Tabella Risultati (Top Right)</h3>
            <div className="grid grid-cols-2 gap-2 text-xs">
              <div className="bg-slate-700/50 rounded p-2">
                <div className="text-slate-400 text-xs">Capitale Iniziale</div>
                <div className="text-white font-semibold text-xs">Per strategia</div>
              </div>
              <div className="bg-slate-700/50 rounded p-2">
                <div className="text-slate-400 text-xs">Capitale Corrente</div>
                <div className="text-emerald-400 font-semibold text-xs">Real-time</div>
              </div>
              <div className="bg-slate-700/50 rounded p-2">
                <div className="text-slate-400 text-xs">P/L Netto</div>
                <div className="text-emerald-400 font-semibold text-xs">Aggregato</div>
              </div>
              <div className="bg-slate-700/50 rounded p-2">
                <div className="text-slate-400 text-xs">Success Rate</div>
                <div className="text-white font-semibold text-xs">Per strategia</div>
              </div>
            </div>
          </div>

          <div className="bg-red-500/10 border border-red-500/30 rounded-xl p-4">
            <h3 className="text-lg font-semibold text-red-300 mb-2">📉 Dettaglio Perdite</h3>
            <p className="text-slate-300 text-xs mb-2">Tabella completa perdite storiche:</p>
            <ul className="space-y-1 text-slate-400 text-xs">
              <li>• Data apertura/chiusura</li>
              <li>• Importo perso ($)</li>
              <li>• Percentuale su capitale investito</li>
              <li>• Motivo chiusura (Margine, KO, etc.)</li>
            </ul>
          </div>

          <div className="bg-blue-500/10 border border-blue-500/30 rounded-xl p-4">
            <h3 className="text-lg font-semibold text-blue-300 mb-2">🎯 Simboli su Grafico</h3>
            <div className="grid grid-cols-2 gap-2 text-xs">
              <div className="flex items-center gap-2">
                <span className="text-base">🟢</span>
                <span className="text-slate-300">Entrata C1</span>
              </div>
              <div className="flex items-center gap-2">
                <span className="text-base">🟡</span>
                <span className="text-slate-300">Entrata Semi-C</span>
              </div>
              <div className="flex items-center gap-2">
                <span className="text-base">🟣</span>
                <span className="text-slate-300">Entrata SCV</span>
              </div>
              <div className="flex items-center gap-2">
                <span className="text-base">✔️</span>
                <span className="text-slate-300">Uscita Profit</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
};

RegisterSlide({
  title: "Dashboard e Monitoraggio",
  order: 8,
})(Slide09Dashboard);

export default Slide09Dashboard;