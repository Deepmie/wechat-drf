<template>
    <div>
        <div style="display: block;">
            <span ref="threecontent">
            </span>
        </div>
    </div>
</template>
<script>
import * as THREE from 'three';
import { OBJLoader } from 'three/examples/jsm/loaders/OBJLoader.js';
import { MTLLoader } from 'three/examples/jsm/loaders/MTLLoader.js';
import { FBXLoader } from 'three/examples/jsm/loaders/FBXLoader.js';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';
import { TGALoader } from 'three/examples/jsm/loaders/TGALoader.js';
import { TextureLoader } from 'three';
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js';
import { FontLoader } from 'three/examples/jsm/loaders/FontLoader.js';
import { TextGeometry } from 'three/examples/jsm/geometries/TextGeometry.js';
import { PLYLoader } from 'three/examples/jsm/loaders/PLYLoader.js';

export default {
    name:"Project",
    data(){
        return {
            point:undefined,
            modeldata:undefined,
            db:undefined,
            modelId:1,
        }
    },
    methods: {
        initThree(){
            // 创建场景
            this.scene = new THREE.Scene()
            // 创建摄像头
            this.camera = new THREE.PerspectiveCamera(75,window.innerWidth / window.innerHeight,0.1,1000)
            this.camera.position.set(0,0,10)
            this.camera.lookAt(0,0,0)

            // 创建渲染器
            this.renderer = new THREE.WebGLRenderer()
            this.renderer.setSize(window.innerWidth, window.innerHeight);
            this.$refs.threecontent.appendChild(this.renderer.domElement);
            // this.$refs.threecontent.addEventListener('mousemove', this.onhover, false);
            
            // 创建控制器
            this.controls = new OrbitControls(this.camera, this.renderer.domElement)

            // 创建环境光
            this.ambientLight = new THREE.AmbientLight(0xffffff, 0.5)
            // 创建直源光
            this.directionalLight = new THREE.DirectionalLight(0xffffff, 1)

            
            this.scene.add(this.ambientLight);
            this.scene.add(this.directionalLight);
        },
        
        async createPLY(){
            console.log("正在加载模型...");
            const loader = new PLYLoader();
            const ModelPath = "http://127.0.0.1:8000/media/d1/mvsnet_3(1).ply"
            loader.load(
                ModelPath,
                (geometry)=>{
                    geometry.computeVertexNormals()
                    const material = new THREE.PointsMaterial({
                        // color:0x0055ff,
                        vertexColors: true,
                        size:0.05
                    })
                    this.point = new THREE.Points(geometry, material)
                    // this.point.rotation.y = Math.PI;
                    // this.point.rotation.x = Math.PI;
                    this.point.position.set(0,0,0)
                    this.scene.add(this.point)
                },
            )

        },

        animate(){
            requestAnimationFrame(this.animate);
            // 写一些更新逻辑的代码
            // console.log(this.point.rotation)
            this.controls.update(); // 启动阻尼时
            // this.point.rotation.y += 0.001;
            // 渲染器对场景和摄像头进行渲染
            this.renderer.render(this.scene,this.camera);
        },

    },
    async mounted() {
        this.initThree();

        // this.createCube()

        this.camera.position.set(0.5,0,-1);
        await this.createPLY();
        // this.camera.lookAt(this.point.position);
        setTimeout(()=>{
            this.animate();
        },1000)
    },

}
</script>
<style lang="css">
    
</style>