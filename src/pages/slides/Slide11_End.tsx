import React from "react";
import { RegisterSlide } from "@/decorators/RegisterSlide";

const Slide11End: React.FC = () => {
  return (
    <section className="relative flex h-full flex-col items-center justify-center text-center px-16">
      {/* Background Image */}
      <div 
        className="absolute inset-0 z-0"
        style={{
          backgroundImage: 'url(/assets/hero-trading-dashboard.jpg)',
          backgroundSize: 'cover',
          backgroundPosition: 'center',
          opacity: 0.2
        }}
      />
      
      {/* Dark Overlay */}
      <div className="absolute inset-0 bg-gradient-to-b from-black/95 to-slate-900/90 z-0" />
      
      {/* Content */}
      <div className="relative z-10 space-y-8">
        <h1 className="text-6xl font-bold text-white tracking-tight mb-6">
          Grazie per l'Attenzione
        </h1>
        
        <div className="max-w-3xl mx-auto space-y-6">
          <div className="bg-slate-800/50 border border-slate-700 rounded-xl p-6">
            <h3 className="text-2xl font-semibold text-emerald-400 mb-4">✨ Vantaggi del Sistema</h3>
            <div className="grid grid-cols-2 gap-4 text-left">
              <div className="flex items-start gap-2">
                <span className="text-emerald-400">✓</span>
                <span className="text-slate-300">Automazione completa</span>
              </div>
              <div className="flex items-start gap-2">
                <span className="text-emerald-400">✓</span>
                <span className="text-slate-300">Gestione rischio avanzata</span>
              </div>
              <div className="flex items-start gap-2">
                <span className="text-emerald-400">✓</span>
                <span className="text-slate-300">Monitoraggio trasparente</span>
              </div>
              <div className="flex items-start gap-2">
                <span className="text-emerald-400">✓</span>
                <span className="text-slate-300">Multi-strategia integrato</span>
              </div>
            </div>
          </div>

          <div className="flex gap-6 justify-center">
            <div className="bg-emerald-500/20 border border-emerald-500 rounded-lg px-8 py-4">
              <div className="text-emerald-400 font-semibold text-lg">Conservativa</div>
              <div className="text-slate-300 text-sm">Stabilità</div>
            </div>
            <div className="bg-amber-500/20 border border-amber-500 rounded-lg px-8 py-4">
              <div className="text-amber-400 font-semibold text-lg">Speculativa</div>
              <div className="text-slate-300 text-sm">Performance</div>
            </div>
            <div className="bg-violet-500/20 border border-violet-500 rounded-lg px-8 py-4">
              <div className="text-violet-400 font-semibold text-lg">SCV</div>
              <div className="text-slate-300 text-sm">Volatilità</div>
            </div>
          </div>
        </div>

        <p className="text-slate-400 text-xl mt-8">
          Sistema di Trading Multi-Strategia • PineScript
        </p>
      </div>
    </section>
  );
};

RegisterSlide({
  title: "Fine",
  order: 9999,
})(Slide11End);

export default Slide11End;