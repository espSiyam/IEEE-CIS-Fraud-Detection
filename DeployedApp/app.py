#import Flask 
from flask import Flask, render_template, request
import numpy as np
import joblib
#create an instance of Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict/', methods=['GET','POST'])
def predict():
    
    if request.method == "POST":
        
        #get form data
        feature_1 = request.form.get('feature_1')
        feature_2 = request.form.get('feature_2')
        feature_3 = request.form.get('feature_3')
        feature_4 = request.form.get('feature_4')
        feature_5 = request.form.get('feature_5')
        feature_6 = request.form.get('feature_6')
        feature_7 = request.form.get('feature_7')
        feature_8 = request.form.get('feature_8')
        feature_9 = request.form.get('feature_9')

        feature_10 = request.form.get('feature_10')
        feature_11 = request.form.get('feature_11')
        feature_12 = request.form.get('feature_12')
        feature_13 = request.form.get('feature_13')
        feature_14 = request.form.get('feature_14')
        feature_15 = request.form.get('feature_15')
        feature_16 = request.form.get('feature_16')
        feature_17 = request.form.get('feature_17')
        feature_18 = request.form.get('feature_18')
        feature_19 = request.form.get('feature_19')

        feature_20 = request.form.get('feature_20')
        feature_21 = request.form.get('feature_21')
        feature_22 = request.form.get('feature_22')
        feature_23 = request.form.get('feature_23')
        feature_24 = request.form.get('feature_24')
        feature_25 = request.form.get('feature_25')
        feature_26 = request.form.get('feature_26')
        feature_27 = request.form.get('feature_27')
        feature_28 = request.form.get('feature_28')
        feature_29 = request.form.get('feature_29')

        feature_30 = request.form.get('feature_30')
        feature_31 = request.form.get('feature_31')
        feature_32 = request.form.get('feature_32')
        feature_33 = request.form.get('feature_33')
        feature_34 = request.form.get('feature_34')
        feature_35 = request.form.get('feature_35')
        feature_36 = request.form.get('feature_36')
        feature_37 = request.form.get('feature_37')
        feature_38 = request.form.get('feature_38')
        feature_39 = request.form.get('feature_39')

        feature_40 = request.form.get('feature_40')
        feature_41 = request.form.get('feature_41')
        feature_42 = request.form.get('feature_42')
        feature_43 = request.form.get('feature_43')
        feature_44 = request.form.get('feature_44')
        feature_45 = request.form.get('feature_45')
        feature_46 = request.form.get('feature_46')
        feature_47 = request.form.get('feature_47')
        feature_48 = request.form.get('feature_48')
        feature_49 = request.form.get('feature_49')

        feature_50 = request.form.get('feature_50')
        feature_51 = request.form.get('feature_51')
        feature_52 = request.form.get('feature_52')
        feature_53 = request.form.get('feature_53')
        feature_54 = request.form.get('feature_54')
        feature_55 = request.form.get('feature_55')
        feature_56 = request.form.get('feature_56')
        feature_57 = request.form.get('feature_57')
        feature_58 = request.form.get('feature_58')
        feature_59 = request.form.get('feature_59')

        feature_60 = request.form.get('feature_60')
        feature_61 = request.form.get('feature_61')
        feature_62 = request.form.get('feature_62')
        feature_63 = request.form.get('feature_63')
        feature_64 = request.form.get('feature_64')
        feature_65 = request.form.get('feature_65')
        feature_66 = request.form.get('feature_66')
        feature_67 = request.form.get('feature_67')
        feature_68 = request.form.get('feature_68')
        feature_69 = request.form.get('feature_69')

        feature_70 = request.form.get('feature_70')
        feature_71 = request.form.get('feature_71')
        feature_72 = request.form.get('feature_72')
        feature_73 = request.form.get('feature_73')
        feature_74 = request.form.get('feature_74')
        feature_75 = request.form.get('feature_75')
        feature_76 = request.form.get('feature_76')
        feature_77 = request.form.get('feature_77')
        feature_78 = request.form.get('feature_78')
        feature_79 = request.form.get('feature_79')

        feature_80 = request.form.get('feature_80')
        feature_81 = request.form.get('feature_81')
        feature_82 = request.form.get('feature_82')
        feature_83 = request.form.get('feature_83')
        feature_84 = request.form.get('feature_84')
        feature_85 = request.form.get('feature_85')
        feature_86 = request.form.get('feature_86')
        feature_87 = request.form.get('feature_87')
        feature_88 = request.form.get('feature_88')
        feature_89 = request.form.get('feature_89')

        feature_90 = request.form.get('feature_90')
        feature_91 = request.form.get('feature_91')
        feature_92 = request.form.get('feature_92')
        feature_93 = request.form.get('feature_93')
        feature_94 = request.form.get('feature_94')
        feature_95 = request.form.get('feature_95')
        feature_96 = request.form.get('feature_96')
        feature_97 = request.form.get('feature_97')
        feature_98 = request.form.get('feature_98')
        feature_99 = request.form.get('feature_99')

        feature_100 = request.form.get('feature_100')
        feature_101 = request.form.get('feature_101')
        feature_102 = request.form.get('feature_102')
        feature_103 = request.form.get('feature_103')
        feature_104 = request.form.get('feature_104')
        feature_105 = request.form.get('feature_105')
        feature_106 = request.form.get('feature_106')
        feature_107 = request.form.get('feature_107')
        feature_108 = request.form.get('feature_108')
        feature_109 = request.form.get('feature_109')
        feature_110 = request.form.get('feature_110')
        feature_111 = request.form.get('feature_111')
        feature_112 = request.form.get('feature_112')
        feature_113 = request.form.get('feature_113')
        feature_114 = request.form.get('feature_114')
        feature_115 = request.form.get('feature_115')
        feature_116 = request.form.get('feature_116')
        feature_117 = request.form.get('feature_117')
        feature_118 = request.form.get('feature_118')
        feature_119 = request.form.get('feature_119')

        feature_120 = request.form.get('feature_120')
        feature_121 = request.form.get('feature_121')
        feature_122 = request.form.get('feature_122')
        feature_123 = request.form.get('feature_123')
        feature_124 = request.form.get('feature_124')
        feature_125 = request.form.get('feature_125')
        feature_126 = request.form.get('feature_126')
        feature_127 = request.form.get('feature_127')
        feature_128 = request.form.get('feature_128')
        feature_129 = request.form.get('feature_129')

        feature_130 = request.form.get('feature_130')
        feature_131 = request.form.get('feature_131')
        feature_132 = request.form.get('feature_132')
        feature_133 = request.form.get('feature_133')
        feature_134 = request.form.get('feature_134')
        feature_135 = request.form.get('feature_135')
        feature_136 = request.form.get('feature_136')
        feature_137 = request.form.get('feature_137')
        feature_138 = request.form.get('feature_138')
        feature_139 = request.form.get('feature_139')

        feature_140 = request.form.get('feature_140')
        feature_141 = request.form.get('feature_141')
        feature_142 = request.form.get('feature_142')
        feature_143 = request.form.get('feature_143')
        feature_144 = request.form.get('feature_144')
        feature_145 = request.form.get('feature_145')
        feature_146 = request.form.get('feature_146')
        feature_147 = request.form.get('feature_147')
        feature_148 = request.form.get('feature_148')
        feature_149 = request.form.get('feature_149')

        feature_150 = request.form.get('feature_150')
        feature_151 = request.form.get('feature_151')
        feature_152 = request.form.get('feature_152')
        feature_153 = request.form.get('feature_153')
        feature_154 = request.form.get('feature_154')
        feature_155 = request.form.get('feature_155')
        feature_156 = request.form.get('feature_156')
        feature_157 = request.form.get('feature_157')
        feature_158 = request.form.get('feature_158')
        feature_159 = request.form.get('feature_159')

        feature_160 = request.form.get('feature_160')
        feature_161 = request.form.get('feature_161')
        feature_162 = request.form.get('feature_162')
        feature_163 = request.form.get('feature_163')
        feature_164 = request.form.get('feature_164')
        feature_165 = request.form.get('feature_165')
        feature_166 = request.form.get('feature_166')
        feature_167 = request.form.get('feature_167')
        feature_168 = request.form.get('feature_168')
        feature_169 = request.form.get('feature_169')

        feature_170 = request.form.get('feature_170')
        feature_171 = request.form.get('feature_171')
        feature_172 = request.form.get('feature_172')
        feature_173 = request.form.get('feature_173')
        feature_174 = request.form.get('feature_174')
        feature_175 = request.form.get('feature_175')
        feature_176 = request.form.get('feature_176')
        feature_177 = request.form.get('feature_177')
        feature_178 = request.form.get('feature_178')
        feature_179 = request.form.get('feature_179')

        feature_180 = request.form.get('feature_180')
        feature_181 = request.form.get('feature_181')
        feature_182 = request.form.get('feature_182')
        feature_183 = request.form.get('feature_183')
        feature_184 = request.form.get('feature_184')
        feature_185 = request.form.get('feature_185')
        feature_186 = request.form.get('feature_186')
        feature_187 = request.form.get('feature_187')
        feature_188 = request.form.get('feature_188')
        feature_189 = request.form.get('feature_189')

        feature_190 = request.form.get('feature_190')
        feature_191 = request.form.get('feature_191')
        feature_192 = request.form.get('feature_192')
        feature_193 = request.form.get('feature_193')
        feature_194 = request.form.get('feature_194')
        feature_195 = request.form.get('feature_195')
        feature_196 = request.form.get('feature_196')
        feature_197 = request.form.get('feature_197')
        feature_198 = request.form.get('feature_198')
        feature_199 = request.form.get('feature_199')
        feature_200 = request.form.get('feature_200')

        feature_201 = request.form.get('feature_201')
        feature_202 = request.form.get('feature_202')
        feature_203 = request.form.get('feature_203')
        feature_204 = request.form.get('feature_204')
        feature_205 = request.form.get('feature_205')
        feature_206 = request.form.get('feature_206')
        feature_207 = request.form.get('feature_207')
        feature_208 = request.form.get('feature_208')
        feature_209 = request.form.get('feature_209')

        feature_210 = request.form.get('feature_210')
        feature_211 = request.form.get('feature_211')
        feature_212 = request.form.get('feature_212')
        feature_213 = request.form.get('feature_213')
        feature_214 = request.form.get('feature_214')
        feature_215 = request.form.get('feature_215')
        feature_216 = request.form.get('feature_216')
        feature_217 = request.form.get('feature_217')
        feature_218 = request.form.get('feature_218')
        feature_219 = request.form.get('feature_219')

        feature_220 = request.form.get('feature_220')
        feature_221 = request.form.get('feature_221')
        feature_222 = request.form.get('feature_222')
        feature_223 = request.form.get('feature_223')
        feature_224 = request.form.get('feature_224')
        feature_225 = request.form.get('feature_225')
        feature_226 = request.form.get('feature_226')
        feature_227 = request.form.get('feature_227')
        feature_228 = request.form.get('feature_228')
        feature_229 = request.form.get('feature_229')

        feature_230 = request.form.get('feature_230')
        feature_231 = request.form.get('feature_231')
        feature_232 = request.form.get('feature_232')
        feature_233 = request.form.get('feature_233')
        feature_234 = request.form.get('feature_234')
        feature_235 = request.form.get('feature_235')
        feature_236 = request.form.get('feature_236')
        feature_237 = request.form.get('feature_237')
        feature_238 = request.form.get('feature_238')
        feature_239 = request.form.get('feature_239')

        feature_240 = request.form.get('feature_240')
        feature_241 = request.form.get('feature_241')
        feature_242 = request.form.get('feature_242')
        feature_243 = request.form.get('feature_243')
        feature_244 = request.form.get('feature_244')
        feature_245 = request.form.get('feature_245')
        feature_246 = request.form.get('feature_246')
        feature_247 = request.form.get('feature_247')
        feature_248 = request.form.get('feature_248')
        feature_249 = request.form.get('feature_249')

        feature_250 = request.form.get('feature_250')
        feature_251 = request.form.get('feature_251')
        feature_252 = request.form.get('feature_252')
        feature_253 = request.form.get('feature_253')
        feature_254 = request.form.get('feature_254')
        feature_255 = request.form.get('feature_255')
        feature_256 = request.form.get('feature_256')
        feature_257 = request.form.get('feature_257')
        feature_258 = request.form.get('feature_258')
        feature_259 = request.form.get('feature_259')

        feature_260 = request.form.get('feature_260')
        feature_261 = request.form.get('feature_261')
        feature_262 = request.form.get('feature_262')
        feature_263 = request.form.get('feature_263')
        feature_264 = request.form.get('feature_264')
        feature_265 = request.form.get('feature_265')
        feature_266 = request.form.get('feature_266')
        feature_267 = request.form.get('feature_267')
        feature_268 = request.form.get('feature_268')
        feature_269 = request.form.get('feature_269')

        feature_270 = request.form.get('feature_270')
        feature_271 = request.form.get('feature_271')
        feature_272 = request.form.get('feature_272')
        feature_273 = request.form.get('feature_273')
        feature_274 = request.form.get('feature_274')
        feature_275 = request.form.get('feature_275')
        feature_276 = request.form.get('feature_276')
        feature_277 = request.form.get('feature_277')
        feature_278 = request.form.get('feature_278')
        feature_279 = request.form.get('feature_279')

        feature_280 = request.form.get('feature_280')
        feature_281 = request.form.get('feature_281')
        feature_282 = request.form.get('feature_282')
        feature_283 = request.form.get('feature_283')
        feature_284 = request.form.get('feature_284')
        feature_285 = request.form.get('feature_285')
        feature_286 = request.form.get('feature_286')
        feature_287 = request.form.get('feature_287')
        feature_288 = request.form.get('feature_288')
        feature_289 = request.form.get('feature_289')

        feature_290 = request.form.get('feature_290')
        feature_291 = request.form.get('feature_291')
        feature_292 = request.form.get('feature_292')
        feature_293 = request.form.get('feature_293')
        feature_294 = request.form.get('feature_294')
        feature_295 = request.form.get('feature_295')
        feature_296 = request.form.get('feature_296')
        feature_297 = request.form.get('feature_297')
        feature_298 = request.form.get('feature_298')

        
        #call preprocessDataAndPredict and pass inputs
        try:
            prediction = preprocessDataAndPredict(feature_1, feature_2, feature_3, feature_4, feature_5, feature_6, feature_7, feature_8, feature_9, feature_10, feature_11, feature_12, 
            	feature_13, feature_14, feature_15, feature_16, feature_17, feature_18, feature_19, feature_20, feature_21, feature_22, feature_23, feature_24, feature_25, feature_26, 
            	feature_27, feature_28, feature_29, feature_30, feature_31, feature_32, feature_33, feature_34, feature_35, feature_36, feature_37, feature_38, feature_39, feature_40, 
            	feature_41, feature_42, feature_43, feature_44, feature_45, feature_46, feature_47, feature_48, feature_49, feature_50, feature_51, feature_52, feature_53, feature_54, 
            	feature_55, feature_56, feature_57, feature_58, feature_59, feature_60, feature_61, feature_62, feature_63, feature_64, feature_65, feature_66, feature_67, feature_68, 
            	feature_69, feature_70, feature_71, feature_72, feature_73, feature_74, feature_75, feature_76, feature_77, feature_78, feature_79, feature_80, feature_81, feature_82, 
            	feature_83, feature_84, feature_85, feature_86, feature_87, feature_88, feature_89, feature_90, feature_91, feature_92, feature_93, feature_94, feature_95, feature_96, 
            	feature_97, feature_98, feature_99, feature_100, feature_101, feature_102, feature_103, feature_104, feature_105, feature_106, feature_107, feature_108, feature_109,
            	feature_110, feature_111, feature_112, feature_113, feature_114, feature_115, feature_116, feature_117, feature_118, feature_119, feature_120, feature_121, feature_122,
            	feature_123, feature_124, feature_125, feature_126, feature_127, feature_128, feature_129, feature_130, feature_131, feature_132, feature_133, feature_134, feature_135, 
            	feature_136, feature_137, feature_138, feature_139, feature_140, feature_141, feature_142, feature_143, feature_144, feature_145, feature_146, feature_147, feature_148, 
            	feature_149, feature_150, feature_151, feature_152, feature_153, feature_154, feature_155, feature_156, feature_157, feature_158, feature_159, feature_160, feature_161, 
            	feature_162, feature_163, feature_164, feature_165, feature_166, feature_167, feature_168, feature_169, feature_170, feature_171, feature_172, feature_173, feature_174, 
            	feature_175, feature_176, feature_177, feature_178, feature_179, feature_180, feature_181, feature_182, feature_183, feature_184, feature_185, feature_186, feature_187, 
            	feature_188, feature_189, feature_190, feature_191, feature_192, feature_193, feature_194, feature_195, feature_196, feature_197, feature_198, feature_199, feature_200, 
            	feature_201, feature_202, feature_203, feature_204, feature_205, feature_206, feature_207, feature_208, feature_209, feature_210, feature_211, feature_212, feature_213, 
            	feature_214, feature_215, feature_216, feature_217, feature_218, feature_219, feature_220, feature_221, feature_222, feature_223, feature_224, feature_225, feature_226, 
            	feature_227, feature_228, feature_229, feature_230, feature_231, feature_232, feature_233, feature_234, feature_235, feature_236, feature_237, feature_238, feature_239, 
            	feature_240, feature_241, feature_242, feature_243, feature_244, feature_245, feature_246, feature_247, feature_248, feature_249, feature_250, feature_251, feature_252, 
            	feature_253, feature_254, feature_255, feature_256, feature_257, feature_258, feature_259, feature_260, feature_261, feature_262, feature_263, feature_264, feature_265, 
            	feature_266, feature_267, feature_268, feature_269, feature_270, feature_271, feature_272, feature_273, feature_274, feature_275, feature_276, feature_277, feature_278, 
            	feature_279, feature_280, feature_281, feature_282, feature_283, feature_284, feature_285, feature_286, feature_287, feature_288, feature_289, feature_290, feature_291, 
            	feature_292, feature_293, feature_294, feature_295, feature_296, feature_297, feature_298)
            #pass prediction to template
            return render_template('predict.html', prediction = prediction)
   
        except ValueError:
            return "Please Enter valid values"
  
        pass
    pass

def preprocessDataAndPredict(feature_1, feature_2, feature_3, feature_4, feature_5, feature_6, feature_7, feature_8, feature_9, feature_10, feature_11, feature_12, 
            	feature_13, feature_14, feature_15, feature_16, feature_17, feature_18, feature_19, feature_20, feature_21, feature_22, feature_23, feature_24, feature_25, feature_26, 
            	feature_27, feature_28, feature_29, feature_30, feature_31, feature_32, feature_33, feature_34, feature_35, feature_36, feature_37, feature_38, feature_39, feature_40, 
            	feature_41, feature_42, feature_43, feature_44, feature_45, feature_46, feature_47, feature_48, feature_49, feature_50, feature_51, feature_52, feature_53, feature_54, 
            	feature_55, feature_56, feature_57, feature_58, feature_59, feature_60, feature_61, feature_62, feature_63, feature_64, feature_65, feature_66, feature_67, feature_68, 
            	feature_69, feature_70, feature_71, feature_72, feature_73, feature_74, feature_75, feature_76, feature_77, feature_78, feature_79, feature_80, feature_81, feature_82, 
            	feature_83, feature_84, feature_85, feature_86, feature_87, feature_88, feature_89, feature_90, feature_91, feature_92, feature_93, feature_94, feature_95, feature_96, 
            	feature_97, feature_98, feature_99, feature_100, feature_101, feature_102, feature_103, feature_104, feature_105, feature_106, feature_107, feature_108, feature_109, 
            	feature_110, feature_111, feature_112, feature_113, feature_114, feature_115, feature_116, feature_117, feature_118, feature_119, feature_120, feature_121, feature_122,
            	feature_123, feature_124, feature_125, feature_126, feature_127, feature_128, feature_129, feature_130, feature_131, feature_132, feature_133, feature_134, feature_135, 
            	feature_136, feature_137, feature_138, feature_139, feature_140, feature_141, feature_142, feature_143, feature_144, feature_145, feature_146, feature_147, feature_148, 
            	feature_149, feature_150, feature_151, feature_152, feature_153, feature_154, feature_155, feature_156, feature_157, feature_158, feature_159, feature_160, feature_161, 
            	feature_162, feature_163, feature_164, feature_165, feature_166, feature_167, feature_168, feature_169, feature_170, feature_171, feature_172, feature_173, feature_174, 
            	feature_175, feature_176, feature_177, feature_178, feature_179, feature_180, feature_181, feature_182, feature_183, feature_184, feature_185, feature_186, feature_187, 
            	feature_188, feature_189, feature_190, feature_191, feature_192, feature_193, feature_194, feature_195, feature_196, feature_197, feature_198, feature_199, feature_200, 
            	feature_201, feature_202, feature_203, feature_204, feature_205, feature_206, feature_207, feature_208, feature_209, feature_210, feature_211, feature_212, feature_213, 
            	feature_214, feature_215, feature_216, feature_217, feature_218, feature_219, feature_220, feature_221, feature_222, feature_223, feature_224, feature_225, feature_226, 
            	feature_227, feature_228, feature_229, feature_230, feature_231, feature_232, feature_233, feature_234, feature_235, feature_236, feature_237, feature_238, feature_239, 
            	feature_240, feature_241, feature_242, feature_243, feature_244, feature_245, feature_246, feature_247, feature_248, feature_249, feature_250, feature_251, feature_252, 
            	feature_253, feature_254, feature_255, feature_256, feature_257, feature_258, feature_259, feature_260, feature_261, feature_262, feature_263, feature_264, feature_265, 
            	feature_266, feature_267, feature_268, feature_269, feature_270, feature_271, feature_272, feature_273, feature_274, feature_275, feature_276, feature_277, feature_278, 
            	feature_279, feature_280, feature_281, feature_282, feature_283, feature_284, feature_285, feature_286, feature_287, feature_288, feature_289, feature_290, feature_291, 
            	feature_292, feature_293, feature_294, feature_295, feature_296, feature_297, feature_298):
    
    #keep all inputs in array
    test_data = [feature_1, feature_2, feature_3, feature_4, feature_5, feature_6, feature_7, feature_8, feature_9, feature_10, feature_11, feature_12, 
            	feature_13, feature_14, feature_15, feature_16, feature_17, feature_18, feature_19, feature_20, feature_21, feature_22, feature_23, feature_24, feature_25, feature_26, 
            	feature_27, feature_28, feature_29, feature_30, feature_31, feature_32, feature_33, feature_34, feature_35, feature_36, feature_37, feature_38, feature_39, feature_40, 
            	feature_41, feature_42, feature_43, feature_44, feature_45, feature_46, feature_47, feature_48, feature_49, feature_50, feature_51, feature_52, feature_53, feature_54, 
            	feature_55, feature_56, feature_57, feature_58, feature_59, feature_60, feature_61, feature_62, feature_63, feature_64, feature_65, feature_66, feature_67, feature_68, 
            	feature_69, feature_70, feature_71, feature_72, feature_73, feature_74, feature_75, feature_76, feature_77, feature_78, feature_79, feature_80, feature_81, feature_82, 
            	feature_83, feature_84, feature_85, feature_86, feature_87, feature_88, feature_89, feature_90, feature_91, feature_92, feature_93, feature_94, feature_95, feature_96, 
            	feature_97, feature_98, feature_99, feature_100, feature_101, feature_102, feature_103, feature_104, feature_105, feature_106, feature_107, feature_108, feature_109, 
            	feature_110, feature_111, feature_112, feature_113, feature_114, feature_115, feature_116, feature_117, feature_118, feature_119, feature_120, feature_121, feature_122,
            	feature_123, feature_124, feature_125, feature_126, feature_127, feature_128, feature_129, feature_130, feature_131, feature_132, feature_133, feature_134, feature_135, 
            	feature_136, feature_137, feature_138, feature_139, feature_140, feature_141, feature_142, feature_143, feature_144, feature_145, feature_146, feature_147, feature_148, 
            	feature_149, feature_150, feature_151, feature_152, feature_153, feature_154, feature_155, feature_156, feature_157, feature_158, feature_159, feature_160, feature_161, 
            	feature_162, feature_163, feature_164, feature_165, feature_166, feature_167, feature_168, feature_169, feature_170, feature_171, feature_172, feature_173, feature_174, 
            	feature_175, feature_176, feature_177, feature_178, feature_179, feature_180, feature_181, feature_182, feature_183, feature_184, feature_185, feature_186, feature_187, 
            	feature_188, feature_189, feature_190, feature_191, feature_192, feature_193, feature_194, feature_195, feature_196, feature_197, feature_198, feature_199, feature_200, 
            	feature_201, feature_202, feature_203, feature_204, feature_205, feature_206, feature_207, feature_208, feature_209, feature_210, feature_211, feature_212, feature_213, 
            	feature_214, feature_215, feature_216, feature_217, feature_218, feature_219, feature_220, feature_221, feature_222, feature_223, feature_224, feature_225, feature_226, 
            	feature_227, feature_228, feature_229, feature_230, feature_231, feature_232, feature_233, feature_234, feature_235, feature_236, feature_237, feature_238, feature_239, 
            	feature_240, feature_241, feature_242, feature_243, feature_244, feature_245, feature_246, feature_247, feature_248, feature_249, feature_250, feature_251, feature_252, 
            	feature_253, feature_254, feature_255, feature_256, feature_257, feature_258, feature_259, feature_260, feature_261, feature_262, feature_263, feature_264, feature_265, 
            	feature_266, feature_267, feature_268, feature_269, feature_270, feature_271, feature_272, feature_273, feature_274, feature_275, feature_276, feature_277, feature_278, 
            	feature_279, feature_280, feature_281, feature_282, feature_283, feature_284, feature_285, feature_286, feature_287, feature_288, feature_289, feature_290, feature_291, 
            	feature_292, feature_293, feature_294, feature_295, feature_296, feature_297, feature_298]
    print(test_data)
    
    #convert value data into numpy array
    test_data = np.array(test_data)
    
    #reshape array
    test_data = test_data.reshape(1,-1)
    print(test_data)
    
    #open file
    file = open("./model/LGBMClassifier.pkl","rb")
    
    #load trained model
    trained_model = joblib.load(file)
    
    #predict
    prediction = trained_model.predict(test_data)
    
    return prediction
    
    pass

if __name__ == '__main__':
    app.run(debug=True)