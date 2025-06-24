// survivor_import_season.js
// Purpose: Import Survivor season data from Fandom and create a vault note.
// Dependencies: fetch, DOMParser, Obsidian API (app, Notice)

async function survivorImportSeason() {
  try {
    const input = window.prompt('Enter Survivor season number:');
    if (!input) {
      new Notice('Import cancelled.');
      return;
    }

    const seasonNumber = parseInt(input.trim(), 10);
    if (Number.isNaN(seasonNumber) || seasonNumber <= 0) {
      new Notice('Invalid season number.');
      return;
    }

    const url = `https://survivor.fandom.com/wiki/Survivor_${seasonNumber}`;
    const res = await fetch(url);
    if (!res.ok) {
      new Notice(`Failed to fetch season ${seasonNumber}.`);
      return;
    }
    const html = await res.text();
    const parser = new DOMParser();
    const doc = parser.parseFromString(html, 'text/html');

    const titleEl = doc.querySelector('h1');
    const title = titleEl ? titleEl.textContent.trim() : `Survivor ${seasonNumber}`;

    const paraEl = doc.querySelector('p');
    let summary = paraEl ? paraEl.textContent : '';
    summary = summary.replace(/\[[0-9]+\]/g, '').replace(/\s+/g, ' ').trim();

    const padded = seasonNumber.toString().padStart(2, '0');
    const folderName = `Survivor/Season ${padded} - ${title.replace(/^Survivor:?\s*/i, '').trim()}`;
    const filePath = `${folderName}/season.md`;

    const frontmatter = `---\nid: survivor-s${padded}\ntitle: ${title}\ntype: season\nnumber: ${seasonNumber}\nsummary: ${summary}\nfolder: ${folderName}\ntags: [survivor, season]\n---\n\n`;

    if (app.vault.getAbstractFileByPath(filePath)) {
      new Notice(`Season file already exists: ${filePath}`);
      return;
    }

    await app.vault.create(filePath, frontmatter);
    new Notice(`Imported ${title}.`);
  } catch (err) {
    console.error(err);
    new Notice('An error occurred while importing.');
  }
}

module.exports = survivorImportSeason;
