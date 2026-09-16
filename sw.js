const CACHE="family-weather-v4-5-3";
const A=["./","./index.html","./styles.css","./app.js","./manifest.webmanifest","./favicon.ico",
"./icons/icon-180.png","./icons/icon-192.png","./icons/icon-512.png","./icons/icon-maskable-512.png"];
self.addEventListener("install",e=>e.waitUntil(caches.open(CACHE).then(c=>c.addAll(A)).then(()=>self.skipWaiting())));
self.addEventListener("activate",e=>e.waitUntil(caches.keys().then(k=>Promise.all(k.filter(x=>x!==CACHE).map(x=>caches.delete(x)))).then(()=>self.clients.claim())));
self.addEventListener("fetch",e=>{
 if(e.request.method==="GET"&&new URL(e.request.url).origin===location.origin)
   e.respondWith(fetch(e.request).catch(()=>caches.match(e.request)));
});