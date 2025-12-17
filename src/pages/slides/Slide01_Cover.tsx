import React from "react";
import { RegisterSlide } from "@/decorators/RegisterSlide";

const Slide01Cover: React.FC = () => {
  return (
    <section className="relative flex h-full flex-col items-center justify-center text-center px-16">
      {/* Background Image */}
      <div 
        className="absolute inset-0 z-0"
        style={{
          backgroundImage: 'url(/assets/hero-trading-dashboard.jpg)',
          backgroundSize: 'cover',
          backgroundPosition: 'center',
          opacity: 0.3
        }}
      />
      
      {/* Dark Overlay */}
      <div className="absolute inset-0 bg-gradient-to-b from-slate-900/90 to-black/95 z-0" />
      
      {/* Content */}
      <div className="relative z-10 space-y-8">
        <h1 className="text-6xl font-bold text-white tracking-tight">
          Sistema di Trading Multi-Strategia
        </h1>
        <p className="text-3xl text-emerald-400 font-semibold">
          Indicatore PineScript Avanzato per Opzioni S&P 500
        </p>
        <div className="flex gap-6 justify-center mt-12">
          <div className="px-6 py-3 bg-emerald-500/20 border border-emerald-500 rounded-lg">
            <span className="text-emerald-400 font-semibold">Conservativa</span>
          </div>
          <div className="px-6 py-3 bg-amber-500/20 border border-amber-500 rounded-lg">
            <span className="text-amber-400 font-semibold">Speculativa</span>
          </div>
          <div className="px-6 py-3 bg-violet-500/20 border border-violet-500 rounded-lg">
            <span className="text-violet-400 font-semibold">SCV</span>
          </div>
        </div>
      </div>
    </section>
  );
};

RegisterSlide({
  title: "Copertina",
  order: 0,
})(Slide01Cover);

export default Slide01Cover;