#!/usr/bin/env python3
"""
Generátor HTML přání ke Dni matek s pixelovou animací krasobruslařů.
Spuštěním vznikne soubor 'den_matek.html', který lze poslat odkazem v e-mailu.
"""

HTML_CONTENT = r"""<!DOCTYPE html>
<html lang="cs">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Všechno nejlepší ke Dni matek!</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  html, body { width: 100%; height: 100%; overflow: hidden; }

  body {
    background: linear-gradient(180deg,
      #b8e0f5 0%,
      #d6ecf7 30%,
      #e8f4fa 60%,
      #f5fafd 100%);
    font-family: 'Courier New', monospace;
    position: relative;
  }

  /* Kluziště přes celou plochu */
  .ice-rink {
    position: fixed;
    inset: 0;
    width: 100vw;
    height: 100vh;
    overflow: hidden;
    background:
      radial-gradient(ellipse at 30% 20%, rgba(255,255,255,0.4) 0%, transparent 50%),
      radial-gradient(ellipse at 70% 80%, rgba(255,255,255,0.3) 0%, transparent 50%),
      linear-gradient(180deg,
        #a8d5ed 0%,
        #c5e1f0 30%,
        #dceef7 60%,
        #ecf6fb 100%);
    image-rendering: pixelated;
  }

  /* Zářící odlesky na ledě */
  .ice-rink::before {
    content: "";
    position: absolute;
    inset: 0;
    background-image:
      radial-gradient(ellipse 200px 80px at 20% 40%, rgba(255,255,255,0.5) 0%, transparent 60%),
      radial-gradient(ellipse 300px 100px at 60% 70%, rgba(255,255,255,0.4) 0%, transparent 60%),
      radial-gradient(ellipse 150px 60px at 85% 25%, rgba(255,255,255,0.5) 0%, transparent 60%),
      radial-gradient(ellipse 250px 90px at 40% 90%, rgba(255,255,255,0.35) 0%, transparent 60%);
    pointer-events: none;
    animation: shimmer 6s ease-in-out infinite;
  }

  @keyframes shimmer {
    0%, 100% { opacity: 0.7; }
    50% { opacity: 1; }
  }

  /* Padající sněhové vločky */
  .snowflake {
    position: fixed;
    top: -10px;
    color: white;
    font-size: 1em;
    animation: fall linear infinite;
    pointer-events: none;
    z-index: 5;
    text-shadow: 0 0 4px rgba(255,255,255,0.8);
  }

  @keyframes fall {
    0% { transform: translateY(0) translateX(0); }
    100% { transform: translateY(110vh) translateX(20px); }
  }

  /* SVG s nápisem psaným bruslařem */
  .writing-svg {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: min(90vw, 1100px);
    height: auto;
    z-index: 3;
    pointer-events: none;
  }

  .writing-path {
    fill: none;
    stroke: #c8e0ed;
    stroke-width: 4;
    stroke-linecap: round;
    stroke-linejoin: round;
    filter: drop-shadow(0 1px 2px rgba(100,150,200,0.5));
    stroke-dasharray: 4500;
    stroke-dashoffset: 4500;
    animation: writeText 18s linear infinite;
  }

  @keyframes writeText {
    0% { stroke-dashoffset: 4500; opacity: 1; }
    70% { stroke-dashoffset: 0; opacity: 1; }
    90% { stroke-dashoffset: 0; opacity: 1; }
    100% { stroke-dashoffset: 0; opacity: 0; }
  }

  /* Bruslař píšící text - posouvá se zleva doprava synchronně s vykreslováním */
  .writer-skater {
    position: absolute;
    top: 50%;
    left: 0;
    width: 50px;
    height: 65px;
    margin-top: -32px;
    z-index: 6;
    animation: writerMove 18s linear infinite;
    image-rendering: pixelated;
  }

  @keyframes writerMove {
    0%   { left: 5%;  top: 50%; opacity: 1; }
    10%  { left: 15%; top: 47%; }
    20%  { left: 25%; top: 53%; }
    30%  { left: 35%; top: 48%; }
    40%  { left: 50%; top: 52%; }
    50%  { left: 65%; top: 48%; }
    60%  { left: 80%; top: 52%; }
    70%  { left: 92%; top: 50%; opacity: 1; }
    85%  { left: 92%; top: 50%; opacity: 1; }
    100% { left: 5%;  top: 50%; opacity: 0; }
  }

  .skater {
    position: absolute;
    image-rendering: pixelated;
    z-index: 4;
  }

  .skater-body {
    width: 100%;
    height: 100%;
    position: relative;
    animation: bounce 0.5s ease-in-out infinite;
  }

  @keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-3px); }
  }

  /* Skater 1 - Mamka v růžovém - oblouky kolem ledu */
  .skater1 {
    width: 60px;
    height: 80px;
    animation: skate1 14s linear infinite;
  }

  @keyframes skate1 {
    0%   { left: 5%;  top: 15%; transform: scaleX(1); }
    20%  { left: 30%; top: 8%;  transform: scaleX(1); }
    35%  { left: 60%; top: 12%; transform: scaleX(1); }
    50%  { left: 85%; top: 20%; transform: scaleX(-1); }
    65%  { left: 75%; top: 80%; transform: scaleX(-1); }
    80%  { left: 40%; top: 85%; transform: scaleX(-1); }
    95%  { left: 10%; top: 75%; transform: scaleX(1); }
    100% { left: 5%;  top: 15%; transform: scaleX(1); }
  }

  /* Skater 2 - prostřední pirueta - VERTIKÁLNÍ rotace (kolem svislé osy) */
  .skater2 {
    width: 55px;
    height: 75px;
    left: 50%;
    top: 50%;
    margin-left: -27px;
    margin-top: -37px;
    animation: skate2Position 16s ease-in-out infinite;
  }

  /* vnitřní wrapper se otáčí kolem svislé osy přes rotateY */
  .skater2 .pirouette {
    width: 100%;
    height: 100%;
    transform-style: preserve-3d;
    animation: pirouetteY 1.6s linear infinite;
  }

  @keyframes pirouetteY {
    0%   { transform: rotateY(0deg); }
    100% { transform: rotateY(360deg); }
  }

  /* Drobná změna pozice piruety, ať to není úplně statické */
  @keyframes skate2Position {
    0%, 100% { margin-left: -27px; margin-top: -37px; }
    25%      { margin-left: 50px;  margin-top: -100px; }
    50%      { margin-left: -100px; margin-top: 20px; }
    75%      { margin-left: 80px;  margin-top: 60px; }
  }

  /* Skater 3 - dítě v modrém - zigzag */
  .skater3 {
    width: 45px;
    height: 60px;
    animation: skate3 11s linear infinite;
  }

  @keyframes skate3 {
    0%   { left: 90%; top: 30%; transform: scaleX(-1); }
    25%  { left: 60%; top: 70%; transform: scaleX(-1); }
    50%  { left: 25%; top: 35%; transform: scaleX(-1); }
    75%  { left: 50%; top: 80%; transform: scaleX(1); }
    100% { left: 90%; top: 30%; transform: scaleX(-1); }
  }

  /* Třpytky */
  .sparkle {
    position: fixed;
    color: #fff;
    pointer-events: none;
    animation: sparkleAnim 3s ease-in-out infinite;
    z-index: 2;
    text-shadow: 0 0 6px rgba(255,255,255,0.9);
  }

  @keyframes sparkleAnim {
    0%, 100% { opacity: 0; transform: scale(0.5); }
    50% { opacity: 1; transform: scale(1.2); }
  }
</style>
</head>
<body>

<div class="ice-rink"></div>

<!-- SVG s nápisem - bruslař ho "vykresluje" jak se posouvá -->
<svg class="writing-svg" viewBox="0 0 1100 200" xmlns="http://www.w3.org/2000/svg">
  <text x="550" y="115"
        text-anchor="middle"
        font-family="'Courier New', monospace"
        font-size="62"
        font-weight="bold"
        class="writing-path">
    Všechno nejlepší ke dni matek!
  </text>
</svg>

<!-- Bruslař, který "píše" text - pohybuje se zleva doprava -->
<div class="writer-skater">
  <svg viewBox="0 0 16 20" width="100%" height="100%" style="image-rendering: pixelated;" shape-rendering="crispEdges">
    <rect x="6" y="0" width="4" height="4" fill="#ffdbac"/>
    <rect x="5" y="0" width="6" height="2" fill="#daa520"/>
    <rect x="6" y="2" width="1" height="1" fill="#000"/>
    <rect x="9" y="2" width="1" height="1" fill="#000"/>
    <rect x="7" y="4" width="2" height="1" fill="#ffdbac"/>
    <rect x="5" y="5" width="6" height="5" fill="#2e8b57"/>
    <rect x="4" y="6" width="1" height="3" fill="#ffdbac"/>
    <rect x="11" y="6" width="1" height="3" fill="#ffdbac"/>
    <rect x="5" y="10" width="6" height="4" fill="#1a4d2e"/>
    <rect x="6" y="14" width="2" height="3" fill="#ffdbac"/>
    <rect x="8" y="14" width="2" height="3" fill="#ffdbac"/>
    <rect x="5" y="17" width="3" height="2" fill="#fff"/>
    <rect x="8" y="17" width="3" height="2" fill="#fff"/>
    <rect x="5" y="19" width="3" height="1" fill="#c0c0c0"/>
    <rect x="8" y="19" width="3" height="1" fill="#c0c0c0"/>
  </svg>
</div>

<!-- Krasobruslař 1 - Mamka v růžovém -->
<div class="skater skater1">
  <div class="skater-body">
    <svg viewBox="0 0 16 20" width="100%" height="100%" style="image-rendering: pixelated;" shape-rendering="crispEdges">
      <rect x="6" y="0" width="4" height="4" fill="#ffdbac"/>
      <rect x="5" y="1" width="1" height="2" fill="#8b4513"/>
      <rect x="10" y="1" width="1" height="2" fill="#8b4513"/>
      <rect x="6" y="0" width="4" height="1" fill="#8b4513"/>
      <rect x="6" y="2" width="1" height="1" fill="#000"/>
      <rect x="9" y="2" width="1" height="1" fill="#000"/>
      <rect x="7" y="4" width="2" height="1" fill="#ffdbac"/>
      <rect x="5" y="5" width="6" height="5" fill="#ff69b4"/>
      <rect x="4" y="6" width="1" height="3" fill="#ffdbac"/>
      <rect x="11" y="6" width="1" height="3" fill="#ffdbac"/>
      <rect x="3" y="10" width="10" height="3" fill="#ff1493"/>
      <rect x="2" y="11" width="12" height="2" fill="#ff69b4"/>
      <rect x="6" y="13" width="2" height="4" fill="#ffdbac"/>
      <rect x="8" y="13" width="2" height="4" fill="#ffdbac"/>
      <rect x="5" y="17" width="3" height="2" fill="#fff"/>
      <rect x="8" y="17" width="3" height="2" fill="#fff"/>
      <rect x="5" y="19" width="3" height="1" fill="#c0c0c0"/>
      <rect x="8" y="19" width="3" height="1" fill="#c0c0c0"/>
    </svg>
  </div>
</div>

<!-- Krasobruslař 2 - prostřední, dělá piruetu kolem svislé osy -->
<div class="skater skater2">
  <div class="pirouette">
    <svg viewBox="0 0 16 20" width="100%" height="100%" style="image-rendering: pixelated;" shape-rendering="crispEdges">
      <rect x="6" y="0" width="4" height="4" fill="#ffdbac"/>
      <rect x="5" y="0" width="6" height="2" fill="#2c1810"/>
      <rect x="6" y="2" width="1" height="1" fill="#000"/>
      <rect x="9" y="2" width="1" height="1" fill="#000"/>
      <rect x="7" y="4" width="2" height="1" fill="#ffdbac"/>
      <rect x="5" y="5" width="6" height="6" fill="#9370db"/>
      <rect x="4" y="3" width="1" height="4" fill="#ffdbac"/>
      <rect x="11" y="3" width="1" height="4" fill="#ffdbac"/>
      <rect x="4" y="2" width="1" height="2" fill="#9370db"/>
      <rect x="11" y="2" width="1" height="2" fill="#9370db"/>
      <rect x="3" y="11" width="10" height="2" fill="#4b0082"/>
      <rect x="4" y="13" width="8" height="1" fill="#9370db"/>
      <rect x="7" y="14" width="2" height="3" fill="#ffdbac"/>
      <rect x="6" y="17" width="4" height="2" fill="#fff"/>
      <rect x="6" y="19" width="4" height="1" fill="#c0c0c0"/>
    </svg>
  </div>
</div>

<!-- Krasobruslař 3 - dítě v modrém -->
<div class="skater skater3">
  <div class="skater-body">
    <svg viewBox="0 0 16 20" width="100%" height="100%" style="image-rendering: pixelated;" shape-rendering="crispEdges">
      <rect x="6" y="1" width="4" height="4" fill="#ffdbac"/>
      <rect x="5" y="0" width="6" height="2" fill="#daa520"/>
      <rect x="6" y="3" width="1" height="1" fill="#000"/>
      <rect x="9" y="3" width="1" height="1" fill="#000"/>
      <rect x="7" y="4" width="2" height="1" fill="#ff69b4"/>
      <rect x="7" y="5" width="2" height="1" fill="#ffdbac"/>
      <rect x="5" y="6" width="6" height="5" fill="#4169e1"/>
      <rect x="4" y="7" width="1" height="3" fill="#ffdbac"/>
      <rect x="11" y="7" width="1" height="3" fill="#ffdbac"/>
      <rect x="4" y="11" width="8" height="3" fill="#1e90ff"/>
      <rect x="6" y="14" width="2" height="3" fill="#ffdbac"/>
      <rect x="8" y="14" width="2" height="3" fill="#ffdbac"/>
      <rect x="5" y="17" width="3" height="2" fill="#fff"/>
      <rect x="8" y="17" width="3" height="2" fill="#fff"/>
      <rect x="5" y="19" width="3" height="1" fill="#c0c0c0"/>
      <rect x="8" y="19" width="3" height="1" fill="#c0c0c0"/>
    </svg>
  </div>
</div>

<script>
  // Generování sněhových vloček
  const symbols = ['❄', '❅', '❆', '✦', '·', '*'];
  const numFlakes = 60;

  for (let i = 0; i < numFlakes; i++) {
    const flake = document.createElement('div');
    flake.className = 'snowflake';
    flake.textContent = symbols[Math.floor(Math.random() * symbols.length)];
    flake.style.left = Math.random() * 100 + 'vw';
    flake.style.animationDuration = (Math.random() * 6 + 5) + 's';
    flake.style.animationDelay = Math.random() * 5 + 's';
    flake.style.fontSize = (Math.random() * 1.2 + 0.5) + 'em';
    flake.style.opacity = Math.random() * 0.7 + 0.3;
    document.body.appendChild(flake);
  }

  // Generování třpytek na ledě
  const numSparkles = 25;
  for (let i = 0; i < numSparkles; i++) {
    const sparkle = document.createElement('div');
    sparkle.className = 'sparkle';
    sparkle.textContent = ['✨', '·', '*', '✦'][Math.floor(Math.random() * 4)];
    sparkle.style.left = Math.random() * 100 + 'vw';
    sparkle.style.top = Math.random() * 100 + 'vh';
    sparkle.style.fontSize = (Math.random() * 0.8 + 0.4) + 'em';
    sparkle.style.animationDelay = Math.random() * 3 + 's';
    sparkle.style.animationDuration = (Math.random() * 2 + 2) + 's';
    document.body.appendChild(sparkle);
  }
</script>

</body>
</html>
"""


def generate_card(output_path: str = "den_matek.html") -> str:
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)
    return output_path


if __name__ == "__main__":
    path = generate_card()
    print(f"Hotovo! HTML přání bylo uloženo do: {path}")
