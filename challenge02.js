/**
 * @param {string[]} names - Array of names to frame
 * @returns {string} The framed names
 */

function createFrame(names) {
  let maxLength = Math.max(...names.map((name) => name.length));
  let border = "*".repeat(maxLength + 4);
  let result = [border];
  for (let name of names) {
    result.push("* " + name.padEnd(maxLength) + " *");
  }
  result.push(border);
  return result.join("\n");
}
