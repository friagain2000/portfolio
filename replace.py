import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_html = """      <div class="skills-layout reveal">
        <!-- Group 1: Design -->
        <div class="skill-category">
          <div class="category-left">
            <h3 class="category-title">Design</h3>
          </div>
          <div class="category-right">
            <div class="skill-row">
              <div class="skill-top">
                <div class="skill-brand">
                  <span class="dot" style="background-color: #31a8ff"></span>
                  <h4 class="name">Adobe Photoshop</h4>
                </div>
                <span class="percent">90%</span>
              </div>
              <p class="desc">고퀄리티 이미지 편집 및 브랜딩 자산 제작이 가능합니다.</p>
              <div class="progress-line"><div class="progress-fill" data-percent="90%"></div></div>
            </div>
            <div class="skill-row">
              <div class="skill-top">
                <div class="skill-brand">
                  <span class="dot" style="background-color: #ff7c00"></span>
                  <h4 class="name">Adobe Illustrator</h4>
                </div>
                <span class="percent">85%</span>
              </div>
              <p class="desc">로고, 아이콘 등 벡터 기반의 그래픽 디자인에 능숙합니다.</p>
              <div class="progress-line"><div class="progress-fill" data-percent="85%"></div></div>
            </div>
            <div class="skill-row">
              <div class="skill-top">
                <div class="skill-brand">
                  <span class="dot" style="background-color: #f24e1e"></span>
                  <h4 class="name">Figma</h4>
                </div>
                <span class="percent">95%</span>
              </div>
              <p class="desc">컴포넌트 중심의 UI 설계 및 프로토타이핑을 지원합니다.</p>
              <div class="progress-line"><div class="progress-fill" data-percent="95%"></div></div>
            </div>
          </div>
        </div>

        <!-- Group 2: Development -->
        <div class="skill-category">
          <div class="category-left">
            <h3 class="category-title">Development</h3>
          </div>
          <div class="category-right">
            <div class="skill-row">
              <div class="skill-top">
                <div class="skill-brand">
                  <span class="dot" style="background-color: #e34f26"></span>
                  <h4 class="name">HTML / CSS</h4>
                </div>
                <span class="percent">95%</span>
              </div>
              <p class="desc">웹 표준을 준수하며 모든 기기에 최적화된 화면을 구현합니다.</p>
              <div class="progress-line"><div class="progress-fill" data-percent="95%"></div></div>
            </div>
            <div class="skill-row">
              <div class="skill-top">
                <div class="skill-brand">
                  <span class="dot" style="background-color: #f7df1e"></span>
                  <h4 class="name">JavaScript</h4>
                </div>
                <span class="percent">85%</span>
              </div>
              <p class="desc">인터랙티브한 동적 요소와 API 연동 로직을 설계합니다.</p>
              <div class="progress-line"><div class="progress-fill" data-percent="85%"></div></div>
            </div>
            <div class="skill-row">
              <div class="skill-top">
                <div class="skill-brand">
                  <span class="dot" style="background-color: #61dafb"></span>
                  <h4 class="name">React</h4>
                </div>
                <span class="percent">80%</span>
              </div>
              <p class="desc">컴포넌트 기반의 효율적인 UI 아키텍처를 구축합니다.</p>
              <div class="progress-line"><div class="progress-fill" data-percent="80%"></div></div>
            </div>
          </div>
        </div>

        <!-- Group 3: Video -->
        <div class="skill-category">
          <div class="category-left">
            <h3 class="category-title">Video</h3>
          </div>
          <div class="category-right">
            <div class="skill-row">
              <div class="skill-top">
                <div class="skill-brand">
                  <span class="dot" style="background-color: #9999ff"></span>
                  <h4 class="name">Adobe Premiere Pro</h4>
                </div>
                <span class="percent">90%</span>
              </div>
              <p class="desc">컷 편집 및 색 보정, 효과적인 스토리텔링이 가능합니다.</p>
              <div class="progress-line"><div class="progress-fill" data-percent="90%"></div></div>
            </div>
            <div class="skill-row">
              <div class="skill-top">
                <div class="skill-brand">
                  <span class="dot" style="background-color: #9999ff"></span>
                  <h4 class="name">Adobe After Effects</h4>
                </div>
                <span class="percent">85%</span>
              </div>
              <p class="desc">화려한 모션 그래픽과 시각 효과를 제작합니다.</p>
              <div class="progress-line"><div class="progress-fill" data-percent="85%"></div></div>
            </div>
          </div>
        </div>

        <!-- Group 4: AI Tech -->
        <div class="skill-category">
          <div class="category-left">
            <h3 class="category-title">AI Tech</h3>
          </div>
          <div class="category-right">
            <div class="skill-row">
              <div class="skill-top">
                <div class="skill-brand">
                  <span class="dot" style="background-color: #20c997"></span>
                  <h4 class="name">Kling</h4>
                </div>
                <span class="percent">95%</span>
              </div>
              <p class="desc">고퀄리티 AI 비디오 생성 및 편집에 능숙합니다.</p>
              <div class="progress-line"><div class="progress-fill" data-percent="95%"></div></div>
            </div>
            <div class="skill-row">
              <div class="skill-top">
                <div class="skill-brand">
                  <span class="dot" style="background-color: #f7df1e"></span>
                  <h4 class="name">Stitch</h4>
                </div>
                <span class="percent">90%</span>
              </div>
              <p class="desc">AI 기반의 창의적인 콘텐츠 결합 및 최적화를 지원합니다.</p>
              <div class="progress-line"><div class="progress-fill" data-percent="90%"></div></div>
            </div>
          </div>
        </div>

        <!-- Group 5: Productivity -->
        <div class="skill-category">
          <div class="category-left">
            <h3 class="category-title">Productivity</h3>
          </div>
          <div class="category-right">
            <div class="skill-row">
              <div class="skill-top">
                <div class="skill-brand">
                  <span class="dot" style="background-color: #191f28"></span>
                  <h4 class="name">GitHub</h4>
                </div>
                <span class="percent">90%</span>
              </div>
              <p class="desc">Git Flow를 활용한 버전 관리 및 원활한 협업이 가능합니다.</p>
              <div class="progress-line"><div class="progress-fill" data-percent="90%"></div></div>
            </div>
            <div class="skill-row">
              <div class="skill-top">
                <div class="skill-brand">
                  <span class="dot" style="background-color: #000000"></span>
                  <h4 class="name">Notion</h4>
                </div>
                <span class="percent">90%</span>
              </div>
              <p class="desc">프로젝트 일정 관리 및 체계적인 문서화를 선호합니다.</p>
              <div class="progress-line"><div class="progress-fill" data-percent="90%"></div></div>
            </div>
          </div>
        </div>
      </div>"""

pattern = re.compile(r'<div class="skills-grid reveal">.*?</section>', re.DOTALL)
new_content = pattern.sub(new_html + '\n    </div>\n  </section>', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Success')