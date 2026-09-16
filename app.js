const GEO="https://geocoding-api.open-meteo.com/v1/search", WEATHER="https://api.open-meteo.com/v1/forecast", AIR="https://air-quality-api.open-meteo.com/v1/air-quality";
const ALIASES={"亚特兰大":"Atlanta","纽约":"New York","纽约市":"New York","西雅图":"Seattle","洛杉矶":"Los Angeles","旧金山":"San Francisco","华盛顿":"Washington","芝加哥":"Chicago","波士顿":"Boston","迈阿密":"Miami","休斯顿":"Houston","伦敦":"London","巴黎":"Paris","东京":"Tokyo","大阪":"Osaka","首尔":"Seoul","新加坡":"Singapore","悉尼":"Sydney","墨尔本":"Melbourne","温哥华":"Vancouver","多伦多":"Toronto"};

const ZH_COUNTRIES={
 "United States":"美国","China":"中国","Canada":"加拿大","Australia":"澳大利亚",
 "United Kingdom":"英国","Japan":"日本","South Korea":"韩国","Singapore":"新加坡",
 "France":"法国","Germany":"德国","Italy":"意大利","Spain":"西班牙","New Zealand":"新西兰"
};
const ZH_ADMIN={
 "Georgia":"佐治亚州","Washington":"华盛顿州","California":"加利福尼亚州","New York":"纽约州",
 "Texas":"德克萨斯州","Illinois":"伊利诺伊州","Massachusetts":"马萨诸塞州","Florida":"佛罗里达州",
 "Guangdong":"广东省","Ontario":"安大略省","British Columbia":"不列颠哥伦比亚省",
 "New South Wales":"新南威尔士州","Victoria":"维多利亚州"
};
const ZH_CITY={
 "Atlanta":"亚特兰大","New York":"纽约","Seattle":"西雅图","Los Angeles":"洛杉矶",
 "San Francisco":"旧金山","Washington":"华盛顿","Chicago":"芝加哥","Boston":"波士顿",
 "Miami":"迈阿密","Houston":"休斯顿","Guangzhou":"广州","London":"伦敦","Paris":"巴黎",
 "Tokyo":"东京","Osaka":"大阪","Seoul":"首尔","Sydney":"悉尼","Melbourne":"墨尔本",
 "Vancouver":"温哥华","Toronto":"多伦多"
};
const EN_CITY={
 "广州":"Guangzhou","深圳":"Shenzhen","北京":"Beijing","上海":"Shanghai","天津":"Tianjin",
 "重庆":"Chongqing","成都":"Chengdu","杭州":"Hangzhou","南京":"Nanjing","武汉":"Wuhan",
 "西安":"Xi'an","苏州":"Suzhou","厦门":"Xiamen","青岛":"Qingdao","长沙":"Changsha",
 "郑州":"Zhengzhou","济南":"Jinan","昆明":"Kunming","福州":"Fuzhou","沈阳":"Shenyang",
 "大连":"Dalian","哈尔滨":"Harbin","长春":"Changchun","石家庄":"Shijiazhuang",
 "合肥":"Hefei","南昌":"Nanchang","南宁":"Nanning","贵阳":"Guiyang","海口":"Haikou",
 "太原":"Taiyuan","兰州":"Lanzhou","乌鲁木齐":"Urumqi","拉萨":"Lhasa","银川":"Yinchuan",
 "西宁":"Xining","呼和浩特":"Hohhot","香港":"Hong Kong","澳门":"Macao","台北":"Taipei"
};
const EN_ADMIN={
 "北京":"Beijing","北京市":"Beijing","上海":"Shanghai","上海市":"Shanghai",
 "天津":"Tianjin","天津市":"Tianjin","重庆":"Chongqing","重庆市":"Chongqing",
 "河北":"Hebei","河北省":"Hebei","山西":"Shanxi","山西省":"Shanxi",
 "辽宁":"Liaoning","辽宁省":"Liaoning","吉林":"Jilin","吉林省":"Jilin",
 "黑龙江":"Heilongjiang","黑龙江省":"Heilongjiang",
 "江苏":"Jiangsu","江苏省":"Jiangsu","浙江":"Zhejiang","浙江省":"Zhejiang",
 "安徽":"Anhui","安徽省":"Anhui","福建":"Fujian","福建省":"Fujian",
 "江西":"Jiangxi","江西省":"Jiangxi","山东":"Shandong","山东省":"Shandong",
 "河南":"Henan","河南省":"Henan","湖北":"Hubei","湖北省":"Hubei",
 "湖南":"Hunan","湖南省":"Hunan","广东":"Guangdong","广东省":"Guangdong",
 "海南":"Hainan","海南省":"Hainan","四川":"Sichuan","四川省":"Sichuan",
 "贵州":"Guizhou","贵州省":"Guizhou","云南":"Yunnan","云南省":"Yunnan",
 "陕西":"Shaanxi","陕西省":"Shaanxi","甘肃":"Gansu","甘肃省":"Gansu",
 "青海":"Qinghai","青海省":"Qinghai",
 "内蒙古":"Inner Mongolia","内蒙古自治区":"Inner Mongolia",
 "广西":"Guangxi","广西壮族自治区":"Guangxi",
 "西藏":"Tibet","西藏自治区":"Tibet",
 "宁夏":"Ningxia","宁夏回族自治区":"Ningxia",
 "新疆":"Xinjiang","新疆维吾尔自治区":"Xinjiang",
 "Georgia":"Georgia","Washington":"Washington","California":"California",
 "New York":"New York","Texas":"Texas","Illinois":"Illinois",
 "Massachusetts":"Massachusetts","Florida":"Florida",
 "Ontario":"Ontario","British Columbia":"British Columbia",
 "New South Wales":"New South Wales","Victoria":"Victoria"
};
const EN_COUNTRY={"中国":"China","美国":"United States","加拿大":"Canada","澳大利亚":"Australia","英国":"United Kingdom","日本":"Japan","韩国":"South Korea","法国":"France","德国":"Germany","意大利":"Italy","西班牙":"Spain","新加坡":"Singapore"};

function specialRegion(x){
 const cc=x.country_code||"";
 const n=x.name||"";
 if(cc==="HK"||n==="香港"||n==="Hong Kong") return lang==="zh"?{city:"香港",admin:"",country:"中国香港"}:{city:"Hong Kong",admin:"",country:"Hong Kong, China"};
 if(cc==="MO"||n==="澳门"||n==="Macao"||n==="Macau") return lang==="zh"?{city:"澳门",admin:"",country:"中国澳门"}:{city:"Macao",admin:"",country:"Macao, China"};
 if(cc==="TW"||x.country==="Taiwan") return lang==="zh"?{city:(n==="Taipei"?"台北":n),admin:x.admin1||"",country:"中国台湾"}:{city:n,admin:x.admin1||"",country:"Taiwan, China"};
 return null;
}
function englishAdmin(v){
 v=String(v||"").trim();
 if(EN_ADMIN[v])return EN_ADMIN[v];
 const stripped=v.replace(/省$|市$|壮族自治区$|维吾尔自治区$|回族自治区$|自治区$/,"");
 return EN_ADMIN[stripped]||v;
}
function displayLocation(x){
 const special=specialRegion(x); if(special)return special;
 if(lang==="zh"){
   return {
     city:x.nameZh||ZH_CITY[x.nameEn||x.name]||x.name,
     admin:x.admin1Zh||ZH_ADMIN[x.admin1En||x.admin1]||x.admin1||"",
     country:x.countryZh||ZH_COUNTRIES[x.countryEn||x.country]||x.country||""
   };
 }
 return {
   city:EN_CITY[x.nameEn]||EN_CITY[x.name]||x.nameEn||x.name,
   admin:englishAdmin(x.admin1En||x.admin1),
   country:EN_COUNTRY[x.countryEn]||EN_COUNTRY[x.country]||x.countryEn||x.country||""
 };
}
function locationLine(x){
 const d=displayLocation(x); return [d.admin,d.country].filter(Boolean).join(" · ");
}
function suggestionLine(x){
 const d=displayLocation(x); return [d.city,d.admin,d.country].filter(Boolean).join(" · ");
}

const T={
zh:{title:"家庭天气",sub:"看看不同城市今天怎么样",add:"添加城市",ph:"广州、亚特兰大、New York…",empty:"搜索城市并点击候选项，就会添加到这里。",none:"没有找到城市",temp:"温度",feel:"体感",rain:"降雨概率",wind:"风速",uv:"UV",air:"空气质量 · US AQI",pm:"PM2.5",compare:"城市对比",time:"当地时间",diff:"与第一个城市时差",tdiff:"温差",hour:"小时",same:"无时差",loading:"正在获取天气与空气质量…",err:"暂时无法获取数据，请稍后重试。",up:"上移",down:"下移",warmer:"更热",cooler:"更冷",sameTemp:"温度相近",faster:"快",slower:"慢"},
en:{title:"Family Weather",sub:"See how today feels across cities",add:"Add city",ph:"Guangzhou, Atlanta, New York…",empty:"Search for a city and tap a suggestion to add it.",none:"No city found",temp:"Temperature",feel:"Feels like",rain:"Rain",wind:"Wind",uv:"UV",air:"Air quality · US AQI",pm:"PM2.5",compare:"City comparison",time:"Local time",diff:"Time difference from first city",tdiff:"Temperature difference",hour:"hours",same:"Same time zone",loading:"Getting weather and air quality…",err:"Data is temporarily unavailable.",up:"Move up",down:"Move down",warmer:"warmer",cooler:"cooler",sameTemp:"similar temperature",faster:"ahead",slower:"behind"}
};
let lang=localStorage.getItem("family-weather-lang")||"zh";
let cities=JSON.parse(localStorage.getItem("family-weather-cities")||"[]"), weatherCache=[];
const input=document.querySelector("#citySearch"),box=document.querySelector("#suggestions"),citiesEl=document.querySelector("#cities"),empty=document.querySelector("#empty"),compare=document.querySelector("#compare"),langEl=document.querySelector("#lang");
let timer,controller; langEl.value=lang;
const esc=s=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const save=()=>localStorage.setItem("family-weather-cities",JSON.stringify(cities));
function canonicalKey(c){return `${Number(c.latitude).toFixed(2)}|${Number(c.longitude).toFixed(2)}`}
function ui(){let t=T[lang];document.documentElement.lang=lang==="zh"?"zh-CN":"en";document.querySelector("#title").textContent=t.title;document.querySelector("#subtitle").textContent=t.sub;document.querySelector("#addLabel").textContent=t.add;input.placeholder=t.ph;empty.textContent=t.empty}
langEl.onchange=()=>{lang=langEl.value;localStorage.setItem("family-weather-lang",lang);ui();render()};
input.addEventListener("input",()=>{clearTimeout(timer);let q=input.value.trim();if(!q){box.classList.add("hidden");return}timer=setTimeout(()=>search(q),180)});
document.addEventListener("click",e=>{if(!e.target.closest(".search-wrap"))box.classList.add("hidden")});
async function geo(q,language){let u=`${GEO}?name=${encodeURIComponent(q)}&count=30&language=${language}&format=json`;return fetch(u,{signal:controller.signal}).then(r=>r.json()).then(d=>d.results||[])}
async function search(q){
 if(controller)controller.abort();controller=new AbortController();
 try{
  let searchQ=ALIASES[q]||q, raw=await geo(searchQ,lang==="zh"?"zh":"en");
  let populated=raw.filter(x=>String(x.feature_code||"").startsWith("P")).sort((a,b)=>(b.population||0)-(a.population||0));
  let seen=new Set(),res=[];
  for(let x of populated){let k=canonicalKey(x);if(seen.has(k))continue;seen.add(k);res.push(x);if(res.length===7)break}
  showSuggestions(res);
 }catch(e){if(e.name!=="AbortError")showSuggestions([])}
}
function showSuggestions(res){let t=T[lang];box.innerHTML=res.length?res.map((x,i)=>`<button class="suggestion" data-i="${i}"><strong>${esc(suggestionLine(x))}</strong></button>`).join(""):`<div class="no-result">${t.none}</div>`;box.classList.remove("hidden");[...box.querySelectorAll("[data-i]")].forEach((e,i)=>e.onclick=()=>add(res[i]))}

function norm(s){return String(s||"").trim().toLowerCase()}
function nearestLocalized(raw,x){
 if(!raw||!raw.length)return null;
 let best=null,score=Infinity;
 for(const r of raw){
   if(!String(r.feature_code||"").startsWith("P"))continue;
   const dy=Number(r.latitude)-Number(x.latitude), dx=Number(r.longitude)-Number(x.longitude);
   const d=dy*dy+dx*dx;
   if(d<score){score=d;best=r}
 }
 return score<0.25?best:null;
}
async function localizedLookup(x,language){
 let qs=[];
 if(language==="en"){
   qs=[x.nameEn,x.name, ...(Object.entries(ALIASES).filter(([z,e])=>norm(z)===norm(x.name)).map(([z,e])=>e))].filter(Boolean);
 }else{
   let reverse=Object.entries(ALIASES).filter(([z,e])=>norm(e)===norm(x.name)||norm(e)===norm(x.nameEn)).map(([z])=>z);
   qs=[...reverse,x.nameZh,x.name].filter(Boolean);
 }
 for(const q of [...new Set(qs)]){
   try{
     let raw=await geo(q,language);
     let hit=nearestLocalized(raw,x);
     if(hit)return hit;
   }catch(e){}
 }
 return null;
}
async function hydrateBilingual(x){
 let [zh,en]=await Promise.all([localizedLookup(x,"zh"),localizedLookup(x,"en")]);
 let base={...x};
 base.nameZh=(zh&&zh.name)||ZH_CITY[(en&&en.name)||x.name]||x.nameZh||x.name;
 base.nameEn=EN_CITY[(en&&en.name)]||EN_CITY[x.name]||(en&&en.name)||x.nameEn||x.name;
 base.admin1Zh=(zh&&zh.admin1)||ZH_ADMIN[(en&&en.admin1)||x.admin1]||x.admin1Zh||x.admin1||"";
 base.admin1En=englishAdmin((en&&en.admin1)||x.admin1En||x.admin1||"");
 base.countryZh=(zh&&zh.country)||ZH_COUNTRIES[(en&&en.country)||x.country]||x.countryZh||x.country||"";
 base.countryEn=EN_COUNTRY[(en&&en.country)]||EN_COUNTRY[x.country]||(en&&en.country)||x.countryEn||x.country||"";
 return base;
}
async function add(x){
 let c={id:x.id,name:x.name,admin1:x.admin1||"",country:x.country,country_code:x.country_code,timezone:x.timezone||"",latitude:x.latitude,longitude:x.longitude};
 c=await hydrateBilingual(c);
 let k=canonicalKey(c);
 let existing=cities.findIndex(v=>canonicalKey(v)===k);
 if(existing>=0)cities[existing]={...cities[existing],...c};
 else cities.push(c);
 save();input.value="";box.classList.add("hidden");render()
}
window.moveCity=(k,dir)=>{
 let i=cities.findIndex(c=>canonicalKey(c)===k),j=i+dir;
 if(i<0||j<0||j>=cities.length)return;
 [cities[i],cities[j]]=[cities[j],cities[i]];save();render()
};
window.removeCity=k=>{cities=cities.filter(c=>canonicalKey(c)!==k);save();render()};
function weatherIcon(c){
 if(c===0)return"☀️"; if([1,2].includes(c))return"🌤️"; if(c===3)return"☁️";
 if([45,48].includes(c))return"🌫️"; if(c>=51&&c<=57)return"🌦️";
 if((c>=61&&c<=67)||(c>=80&&c<=82))return"🌧️";
 if((c>=71&&c<=77)||(c>=85&&c<=86))return"🌨️"; if(c>=95)return"⛈️"; return"🌡️"
}
function wlabel(c){if(lang==="en"){if(c===0)return"Clear";if([1,2].includes(c))return"Mostly clear / partly cloudy";if(c===3)return"Overcast";if([45,48].includes(c))return"Fog";if(c>=51&&c<=57)return"Drizzle";if((c>=61&&c<=67)||(c>=80&&c<=82))return"Rain";if((c>=71&&c<=77)||(c>=85&&c<=86))return"Snow";if(c>=95)return"Thunderstorm";return"Other"}if(c===0)return"晴朗";if([1,2].includes(c))return"晴到多云";if(c===3)return"阴天";if([45,48].includes(c))return"有雾";if(c>=51&&c<=57)return"毛毛雨";if((c>=61&&c<=67)||(c>=80&&c<=82))return"有雨";if((c>=71&&c<=77)||(c>=85&&c<=86))return"有雪";if(c>=95)return"雷暴";return"其他"}
function aqi(a){if(lang==="en")return a<=50?"Good":a<=100?"Moderate":a<=150?"Unhealthy for sensitive groups":a<=200?"Unhealthy":a<=300?"Very unhealthy":"Hazardous";return a<=50?"优":a<=100?"中等":a<=150?"敏感人群不健康":a<=200?"不健康":a<=300?"非常不健康":"危险"}
function uvl(u){if(lang==="en")return u<3?"Low":u<6?"Moderate":u<8?"High":u<11?"Very high":"Extreme";return u<3?"低":u<6?"中等":u<8?"高":u<11?"很高":"极高"}
function advice(r,temp,uv,a){if(lang==="en")return[(r>=50?"Bring an umbrella today.":r>=30?"An umbrella may be useful.":"An umbrella is probably not needed."),(temp>=30?"Wear light, breathable clothing.":temp>=20?"Light clothing should be comfortable.":temp>=10?"A light jacket may help.":"Dress warmly."),(uv>=6?"UV is strong; use sun protection.":uv>=3?"Consider sun protection for long outdoor exposure.":"UV is relatively low."),(a>150?"Air quality is poor; reduce prolonged outdoor activity.":a>100?"Sensitive groups may reduce prolonged outdoor activity.":"No major air-quality restriction right now.")];return[(r>=50?"今天建议带伞。":r>=30?"有一定降雨可能，带把伞更稳妥。":"今天通常不用带伞。"),(temp>=30?"天气较热，穿轻薄透气的衣服。":temp>=20?"短袖或轻薄衣物通常比较舒服。":temp>=10?"天气偏凉，建议加一件薄外套。":"天气较冷，注意保暖。"),(uv>=6?"紫外线较强，外出建议做好防晒。":uv>=3?"长时间户外活动建议做好防晒。":"紫外线较低。"),(a>150?"空气质量较差，尽量减少长时间户外活动。":a>100?"敏感人群可适当减少长时间户外活动。":"空气质量目前没有明显限制。")]}
function local(tz){let n=new Date(),locale=lang==="zh"?"zh-CN":"en-US";return{date:new Intl.DateTimeFormat(locale,{timeZone:tz,year:"numeric",month:lang==="zh"?"long":"short",day:"numeric",weekday:"short"}).format(n),time:new Intl.DateTimeFormat(locale,{timeZone:tz,hour:"2-digit",minute:"2-digit",hour12:false}).format(n)}}
async function fetchData(c){let wp=new URLSearchParams({latitude:c.latitude,longitude:c.longitude,current:"temperature_2m,apparent_temperature,weather_code,wind_speed_10m",daily:"precipitation_probability_max,uv_index_max",timezone:"auto",forecast_days:"1"}),ap=new URLSearchParams({latitude:c.latitude,longitude:c.longitude,current:"us_aqi,pm2_5",timezone:"auto"});let[w,a]=await Promise.all([fetch(`${WEATHER}?${wp}`).then(r=>r.json()),fetch(`${AIR}?${ap}`).then(r=>r.json())]);return{w,a}}
async function render(){
 ui();let t=T[lang];empty.style.display=cities.length?"none":"block";compare.classList.add("hidden");weatherCache=[];
 citiesEl.innerHTML=cities.map(c=>{let d=displayLocation(c);return `<article class="card" id="c-${c.id}"><div class="card-top"><div><h2>${esc(d.city)}</h2><div class="country">${esc(locationLine(c))}</div></div><div class="card-actions"><button class="move" onclick="moveCity('${canonicalKey(c)}',-1)" title="${t.up}">↑</button><button class="move" onclick="moveCity('${canonicalKey(c)}',1)" title="${t.down}">↓</button><button class="remove" onclick="removeCity('${canonicalKey(c)}')">×</button></div></div><div class="loading">${t.loading}</div></article>`}).join("");
 for(let c of cities){let el=document.getElementById(`c-${c.id}`);try{let{w,a}=await fetchData(c),cur=w.current,aq=a.current||{},dt=local(w.timezone),rain=w.daily?.precipitation_probability_max?.[0]??0,uv=w.daily?.uv_index_max?.[0]??0,A=aq.us_aqi??0,pm=aq.pm2_5??0,adv=advice(rain,cur.apparent_temperature,uv,A);weatherCache.push({c,w,temp:cur.temperature_2m,time:dt.time});
 let dl=displayLocation(c); el.innerHTML=`<div class="card-top"><div><h2>${esc(dl.city)}</h2><div class="country">${esc(locationLine(c))}</div></div><div class="card-actions"><button class="move" onclick="moveCity('${canonicalKey(c)}',-1)" title="${t.up}">↑</button><button class="move" onclick="moveCity('${canonicalKey(c)}',1)" title="${t.down}">↓</button><button class="remove" onclick="removeCity('${canonicalKey(c)}')">×</button></div></div><div class="datetime">📅 ${esc(dt.date)}　🕐 ${esc(dt.time)}</div><div class="hero"><div class="temp-block"><div class="weather-icon">${weatherIcon(cur.weather_code)}</div><div class="temp">${Math.round(cur.temperature_2m)}°</div></div><div class="condition">${wlabel(cur.weather_code)}<br><span>${t.feel} ${Math.round(cur.apparent_temperature)}°C</span></div></div><div class="metrics"><div class="metric"><small>${t.rain}</small><b>${rain}%</b></div><div class="metric"><small>${t.wind}</small><b>${Math.round(cur.wind_speed_10m)} km/h</b></div><div class="metric"><small>${t.uv}</small><b>${uv.toFixed(1)} · ${uvl(uv)}</b></div><div class="metric"><small>${t.air}</small><b>${Math.round(A)} · ${aqi(A)}</b></div><div class="metric"><small>${t.pm}</small><b>${pm.toFixed(1)} μg/m³</b></div></div><div class="advice"><div>☂️ <span>${adv[0]}</span></div><div>👕 <span>${adv[1]}</span></div><div>🧴 <span>${adv[2]}</span></div><div>🌿 <span>${adv[3]}</span></div></div>`;
 }catch(e){el.querySelector(".loading").textContent=t.err}}
 renderCompare()
}
function renderCompare(){
 if(weatherCache.length<2)return;
 let t=T[lang];
 let rows=weatherCache.map(x=>`<div class="compare-city"><b>${esc(displayLocation(x.c).city)}</b><span>${weatherIcon(x.w.current.weather_code)} ${Math.round(x.temp)}°C</span><small>${esc(x.time)}</small></div>`).join("");
 let pairs=[];
 for(let i=0;i<weatherCache.length;i++){
  for(let j=i+1;j<weatherCache.length;j++){
   let a=weatherCache[i],b=weatherCache[j];
   let dh=(b.w.utc_offset_seconds-a.w.utc_offset_seconds)/3600;
   let td=b.temp-a.temp;
   let timeText=dh===0?t.same:(lang==="zh"?(dh>0?`${displayLocation(b.c).city}比${displayLocation(a.c).city}${t.faster} ${dh} ${t.hour}`:`${displayLocation(b.c).city}比${displayLocation(a.c).city}${t.slower} ${Math.abs(dh)} ${t.hour}`):(dh>0?`${displayLocation(b.c).city} is ${dh} ${t.hour} ${t.faster}`:`${displayLocation(b.c).city} is ${Math.abs(dh)} ${t.hour} ${t.slower}`));
   let tempText=Math.abs(td)<0.5?t.sameTemp:(lang==="zh"?(td>0?`${displayLocation(b.c).city}约${t.warmer} ${Math.abs(td).toFixed(1)}°C`:`${displayLocation(b.c).city}约${t.cooler} ${Math.abs(td).toFixed(1)}°C`):(td>0?`${displayLocation(b.c).city} is ${Math.abs(td).toFixed(1)}°C ${t.warmer}`:`${displayLocation(b.c).city} is ${Math.abs(td).toFixed(1)}°C ${t.cooler}`));
   pairs.push(`<div><b>${esc(displayLocation(a.c).city)} ↔ ${esc(displayLocation(b.c).city)}</b><span>${esc(timeText)} · ${esc(tempText)}</span></div>`);
  }
 }
 compare.innerHTML=`<h2>${t.compare}</h2><div class="compare-grid">${rows}</div><div class="diffs">${pairs.join("")}</div>`;
 compare.classList.remove("hidden")
}
async function migrateCities(){
 let changed=false;
 for(let i=0;i<cities.length;i++){
   let c=cities[i];
   if(!c.nameZh||!c.nameEn||!c.countryZh||!c.countryEn){
     try{cities[i]=await hydrateBilingual(c);changed=true}catch(e){}
   }
 }
 if(changed)save();
}
ui();migrateCities().then(render);
if("serviceWorker"in navigator)window.addEventListener("load",()=>navigator.serviceWorker.register("./sw.js"));
