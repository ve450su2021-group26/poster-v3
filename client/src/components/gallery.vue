<template>
  <div>
    <div id="container"></div>
  </div>
</template>

<script>
//import from the node_modules
import * as THREE from '../../node_modules/three/build/three.module.js';
import {PCFSoftShadowMap} from '../../node_modules/three/build/three.module.js';
import Stats from '../../node_modules/three/examples/jsm/libs/stats.module.js';
import { OrbitControls } from '../../node_modules/three/examples/jsm/controls/OrbitControls.js';

export default {
  name: 'gallery',
  data () {
    return {
      camera: null,
      scene: null,
      controls: null,
      stats: null,
      renderer: null,
      rayCaster: null,
      inter: new THREE.Group(),
      posterPairs: null,
      num: 3,
      pointer: new THREE.Vector2(),
      nameList: ['Wenxin', 'Keji', "Jianyue", "Xiqing", "Qingxin", "Fugu", "Shangwu", "Xuanku", "Menghuan"],
      candidate: [this.nameList[Math.floor(Math.random()*10)], this.nameList[Math.floor(Math.random()*10)], this.nameList[Math.floor(Math.random()*10)]],
    }
  },
  methods: {
    loadText: function(text, x, y, z, angle, i){
      let loader = new THREE.FontLoader();
      loader.load( '../../node_modules/three/examples/fonts/optimer_bold.typeface.json', function ( font ) {
        let textGeometry = new THREE.TextBufferGeometry( text, {
          font: font,
          size: 1,
          height: 0.1,
        } );
        textGeometry.computeBoundingBox();
        let mesh = new THREE.Mesh(textGeometry, new THREE.MeshLambertMaterial({color:0xffffff}));
        mesh.material.emissive.setHex(0xffffff);
        mesh.position.x = -text.length/3;
        mesh.position.y = 0;
        mesh.position.z = 0;
        let pivot = new THREE.Object3D();
        pivot.position.set(x, y, z);
        this.scene.add(pivot);
        pivot.add(mesh);
        console.log(mesh.position);
        pivot.rotation.y = angle;
        this.posterPairs[i]["text"] = mesh;
      } );
    },
    init: function () {
      //number of the recommended posters
      //initialize container
      let container = document.getElementById("container");
      document.body.appendChild(container);

      //initialize the camera
      this.camera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 1, 1000);
      this.camera.setLens(8);
      //camera.lookAt(new THREE.Vector3(0, 0, 0));
      this.camera.position.set(0, 0, this.num*3+14);
      //initialize the scene
      this.scene = new THREE.Scene();
      this.scene.add(new THREE.AmbientLight(0xffffff, 0.5));
      //initialize the outside box of the gallery
      let box = new THREE.BoxGeometry(30, 15, this.num*3+16);
      let outside = new THREE.Mesh( box, new THREE.MeshPhongMaterial( { color: 0xffffff } ) );
      outside.position.x = 0;
      outside.position.y = 0;
      outside.position.z = this.num*3/2+8;
      //object.rotation.x= -Math.PI/2;
      outside.receiveShadow = true;
      outside.material.side = THREE.DoubleSide;
      this.scene.add(outside);
      //initialize the renderer
      this.renderer = new THREE.WebGLRenderer();
      this.renderer.setSize(window.innerWidth, window.innerHeight);
      this.renderer.shadowMap.enabled = true;
      this.renderer.shadowMap.type = PCFSoftShadowMap;
      document.body.appendChild(this.renderer.domElement);
      //add orbital controls to the camera
      this.controls = new OrbitControls( this.camera, this.renderer.domElement );
      this.controls.update();
      //initialize raycaster
      this.rayCaster = new THREE.Raycaster();
      //save the current render situation
      container.appendChild(this.renderer.domElement);
      this.stats = new Stats();
      container.appendChild(this.stats.dom);
      //add listener to the mouse move
      document.addEventListener('mousemove', onPointerMove);
      function onPointerMove(event) {
        this.pointer.x = (event.clientX / window.innerWidth) * 2 - 1;
        this.pointer.y = -(event.clientY / window.innerHeight) * 2 + 1;
      }
      //initialize poster and light array
      for (let i = 0; i < this.num; i++) {
        let plane = new THREE.PlaneGeometry(5, 4, 32);
        const texture = new THREE.TextureLoader().load("./"+this.candidate[i]+".png");

        //now just set the material and color as random
        const object = new THREE.Mesh(plane, new THREE.MeshLambertMaterial({color: 0xffffff, map: texture, emissiveIntensity: 0.5,emissive: 0xffffff, emissiveMap: texture}));
        //set the position ans rotation of the objects
        object.position.x = 5 * Math.pow(-1, i % 2);
        object.position.y = 0;
        object.position.z = this.num*3+8-3*i;
        object.rotation.y = -Math.PI / 6 * Math.pow(-1, i % 2);
        object.castShadow = true;
        object.material.side = THREE.DoubleSide;
        this.inter.add(object);

        //set the position of the spot light
        const spotLight = new THREE.SpotLight(0xffffff, 0.1);
        spotLight.position.x = 5 * Math.pow(-1, i % 2);
        spotLight.position.y = 4;
        spotLight.position.z = this.num*3+8-3*i;
        spotLight.angle = Math.PI/6;
        spotLight.penumbra = 0.5;
        let lightTarget = new THREE.Object3D();
        lightTarget.position.x = 5 * Math.pow(-1, i % 2);
        lightTarget.position.y = -4;
        lightTarget.position.z = this.num*3+8-3*i;
        this.scene.add(lightTarget);
        spotLight.target = lightTarget;
        spotLight.castShadow = true;
        this.scene.add(spotLight);
        //var helper = new THREE.CameraHelper( spotLight.shadow.camera );
        //scene.add( helper );
        this.posterPairs[i] = {poster: object, light: spotLight};
        this.loadText(this.candidate[i], 5 * Math.pow(-1, i % 2), 3, this.num*3+8-3*i, -Math.PI / 6 * Math.pow(-1, i % 2), i);
      }
      this.scene.add(this.inter);
    },
    render: function(){
      let INTERSECTED;
      this.rayCaster.setFromCamera( this.pointer, this.camera );
      const intersects = this.rayCaster.intersectObjects( this.inter.children );
      //find the first object intersected and let it emit red color
      if ( intersects.length > 0) {
        if ( INTERSECTED !== intersects[0].object) {
          if ( INTERSECTED ) INTERSECTED.material.emissive.setHex( INTERSECTED.currentHex );
          INTERSECTED = intersects[0].object;
          INTERSECTED.currentHex = INTERSECTED.material.emissive.getHex();
          INTERSECTED.material.emissive.setHex( 0xff0000 );
          let ind = (this.num*3+8-INTERSECTED.position.z)/3;
          this.posterPairs[ind].light.intensity = 0.5;
          this.posterPairs[ind]["text"].material.emissive.setHex( 0xff0000 );
          //set the case when some object is selected and the mouse clicked
          document.onclick = function (e){
            console.log("./"+this.candidate[ind]+".html");
            window.open("./"+this.candidate[ind]+".html");
          }
        }
        //recome to the original color
      } else {
        if ( INTERSECTED ) {
          INTERSECTED.material.emissive.setHex(INTERSECTED.currentHex);
          let ind = (this.num * 3 + 8 - INTERSECTED.position.z) / 3;
          this.posterPairs[ind].light.intensity = 0.1;
          this.posterPairs[ind]["text"].material.emissive.setHex( 0xffffff );
          INTERSECTED = null;
        }
      }
      renderer.render(this.scene, this.camera);
    },
    animate: function () {
      requestAnimationFrame(this.animate);
      const boxBound = new THREE.Box3(new THREE.Vector3(-8, -4, 2), new THREE.Vector3(8, 4, this.num*3+14));
      if(this.camera.position.x > boxBound.max.x){
        this.camera.position.x = boxBound.max.x;
      }

      if(this.camera.position.x < boxBound.min.x){
        this.camera.position.x = boxBound.min.x;
      }

      if(this.camera.position.z > boxBound.max.z){
        this.camera.position.z = boxBound.max.z;
      }

      if(this.camera.position.z < boxBound.min.z){
        this.camera.position.z = boxBound.min.z;
      }

      if(this.camera.position.y > boxBound.max.y){
        this.camera.position.y = boxBound.max.y;
      }

      if(this.camera.position.y < boxBound.min.y){
        this.camera.position.y = boxBound.min.y;
      }
      this.controls.update();
      this.render();
      this.stats.update();
    }
  },
  mounted () {
    this.init()
    this.animate()
  }
}
</script>
<style scoped>
#container {
  height: 400px;
}
</style>
