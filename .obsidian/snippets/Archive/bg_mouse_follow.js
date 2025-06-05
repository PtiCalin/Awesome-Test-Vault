
document.addEventListener('mousemove', (e) => {
  const x = e.clientX / window.innerWidth - 0.5;
  const y = e.clientY / window.innerHeight - 0.5;
  const resistance = 20;

  document.body.style.setProperty('--bg-x', `${x * resistance}px`);
  document.body.style.setProperty('--bg-y', `${y * resistance}px`);
});
