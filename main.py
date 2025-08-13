import React, { useState } from "react";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

export default function ExerciseRecommendation() {
  const [step, setStep] = useState(1);
  const [answers, setAnswers] = useState({
    fitnessLevel: "",
    skillLevel: "",
    environment: "",
    goal: "",
  });
  const [recommendation, setRecommendation] = useState(null);

  const exercises = [
    {
      name: "수영",
      difficulty: "중간",
      description: "전신 근육을 고르게 사용하며 심폐지구력을 향상시키는 운동입니다.",
      criteria: { fitness: "중간", skill: "중간", environment: "실내", goal: "체력 향상" },
    },
    {
      name: "러닝",
      difficulty: "쉬움~중간",
      description: "심폐지구력 향상과 체중 감량에 좋은 대표적인 유산소 운동입니다.",
      criteria: { fitness: "낮음", skill: "초보", environment: "야외", goal: "체중 감량" },
    },
    {
      name: "요가",
      difficulty: "쉬움",
      description: "유연성과 집중력을 향상시키며 스트레스 완화에 도움을 줍니다.",
      criteria: { fitness: "낮음", skill: "초보", environment: "실내", goal: "유연성 향상" },
    },
    {
      name: "크로스핏",
      difficulty: "높음",
      description: "고강도 전신 운동으로 근력과 지구력을 동시에 향상시킵니다.",
      criteria: { fitness: "높음", skill: "중급", environment: "실내", goal: "근력 강화" },
    },
    {
      name: "등산",
      difficulty: "중간~높음",
      description: "심폐지구력과 하체 근력을 향상시키며 자연 속에서 운동할 수 있습니다.",
      criteria: { fitness: "중간", skill: "중급", environment: "야외", goal: "체력 향상" },
    },
    {
      name: "필라테스",
      difficulty: "쉬움~중간",
      description: "코어 근육 강화와 자세 교정에 탁월한 실내 운동입니다.",
      criteria: { fitness: "낮음", skill: "초보", environment: "실내", goal: "자세 교정" },
    },
    {
      name: "자전거 타기",
      difficulty: "쉬움~중간",
      description: "하체 근육 강화와 심폐지구력 향상에 좋은 유산소 운동입니다.",
      criteria: { fitness: "중간", skill: "중급", environment: "야외", goal: "체력 향상" },
    },
  ];

  const handleAnswer = (question, value) => {
    setAnswers({ ...answers, [question]: value });
  };

  const handleRecommendation = () => {
    const found = exercises.find(
      (ex) =>
        ex.criteria.fitness === answers.fitnessLevel &&
        ex.criteria.skill === answers.skillLevel &&
        ex.criteria.environment === answers.environment &&
        ex.criteria.goal === answers.goal
    );
    setRecommendation(found || { name: "추천 없음", difficulty: "-", description: "조건에 맞는 운동이 없습니다." });
    setStep(3);
  };

  return (
    <div className="p-6 max-w-xl mx-auto">
      {step === 1 && (
        <Card>
          <CardHeader>
            <CardTitle>1단계: 체력 및 기술 설문</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="font-semibold">현재 체력 수준은?</p>
            <div className="flex gap-2 my-2">
              {["낮음", "중간", "높음"].map((level) => (
                <Button key={level} onClick={() => handleAnswer("fitnessLevel", level)}>
                  {level}
                </Button>
              ))}
            </div>

            <p className="font-semibold mt-4">해당 운동에 대한 기술 수준은?</p>
            <div className="flex gap-2 my-2">
              {["초보", "중간", "중급", "고급"].map((level) => (
                <Button key={level} onClick={() => handleAnswer("skillLevel", level)}>
                  {level}
                </Button>
              ))}
            </div>

            <p className="font-semibold mt-4">선호하는 운동 환경은?</p>
            <div className="flex gap-2 my-2">
              {["실내", "야외"].map((env) => (
                <Button key={env} onClick={() => handleAnswer("environment", env)}>
                  {env}
                </Button>
              ))}
            </div>

            <p className="font-semibold mt-4">운동 목표는?</p>
            <div className="flex gap-2 my-2">
              {["체력 향상", "체중 감량", "근력 강화", "유연성 향상", "자세 교정"].map((goal) => (
                <Button key={goal} onClick={() => handleAnswer("goal", goal)}>
                  {goal}
                </Button>
              ))}
            </div>

            <Button className="mt-4" onClick={() => setStep(2)}>
              다음
            </Button>
          </CardContent>
        </Card>
      )}

      {step === 2 && (
        <Card>
          <CardHeader>
            <CardTitle>설문 결과 확인</CardTitle>
          </CardHeader>
          <CardContent>
            <p>체력 수준: {answers.fitnessLevel}</p>
            <p>기술 수준: {answers.skillLevel}</p>
            <p>환경: {answers.environment}</p>
            <p>목표: {answers.goal}</p>
            <Button className="mt-4" onClick={handleRecommendation}>
              운동 추천 받기
            </Button>
          </CardContent>
        </Card>
      )}

      {step === 3 && recommendation && (
        <Card>
          <CardHeader>
            <CardTitle>추천 운동</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="font-bold text-lg">{recommendation.name}</p>
            <p>난이도: {recommendation.difficulty}</p>
            <p>설명: {recommendation.description}</p>
            <Button className="mt-4" onClick={() => setStep(1)}>
              다시 하기
            </Button>
          </CardContent>
        </Card>
      )}
    </div>
  );
}
