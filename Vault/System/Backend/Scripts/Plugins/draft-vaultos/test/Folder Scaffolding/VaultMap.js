/**
 * VaultMap.js
 * Interactive Vault Map Overlay Engine
 */

export class VaultMap {
  constructor(options) {
    this.vaultName = options.vaultName || "Unnamed Vault";
    this.mapElementId = "vault-map-wrapper";
    this.zones = [
      {
        name: "🧠 System",
        points: "100,100 200,100 200,200 100,200",
        link: "System"
      },
      {
        name: "📚 Encyclopedia",
        points: "220,100 320,100 320,200 220,200",
        link: "Encyclopedia"
      },
      {
        name: "💘 Learnings",
        points: "340,100 440,100 440,200 340,200",
        link: "Learnings"
      }
    ];
  }

  renderMap() {
    const wrapper = document.getElementById(this.mapElementId);
    if (!wrapper) return;

    let svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("width", "100%");
    svg.setAttribute("height", "100%");
    svg.style.position = "absolute";
    svg.style.top = "0";
    svg.style.left = "0";

    this.zones.forEach(zone => {
      let poly = document.createElementNS("http://www.w3.org/2000/svg", "polygon");
      poly.setAttribute("points", zone.points);
      poly.setAttribute("class", "hotspot");
      poly.addEventListener("click", () => {
        window.open(zone.link + ".md", "_self");
      });
      poly.setAttribute("title", zone.name);
      svg.appendChild(poly);
    });

    wrapper.appendChild(svg);
  }
}