const contents = await Deno.readTextFile("./data.json");
console.log(contents);

const pipInstall = Deno.run({
  cmd: ["python", "-m", "pip", "install", "-r", "requirements.txt"],
});

await pipInstall.status();

const pyRun = Deno.run({
  cmd: ['python', './postprocessing.py'],
});

await pyRun.status();
