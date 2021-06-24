const contents = await Deno.readTextFile("./data.json");
console.log(contents);

const pip_install = Deno.run({
  cmd: ["python", "-m", "pip", "install", "-r", "requirements.txt"],
});

await pip_install.status();

const py_run = Deno.run({
  cmd: ['python', './postprocessing.py'],
});

await py_run.status();
