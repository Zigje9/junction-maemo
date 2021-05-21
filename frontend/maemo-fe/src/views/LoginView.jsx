import React from 'react';
import InputTitle from "../components/LoginView/div/title";
import Input from "../components/LoginView/input/input";
import RelateType from "../components/LoginView/input/relateType";
import RelateOption from "../components/LoginView/input/relateOption";
import SubmitButton from "../components/LoginView/button/submitButton";

const LoginView = () => {
  return (
    <>
    <InputTitle>이름</InputTitle>
    <Input placeholder="이름을 입력하세요."></Input>
    <InputTitle>전화번호</InputTitle>
    <Input placeholder="전화번호를 입력하세요."></Input>
    <InputTitle>장애유형</InputTitle>
    <Input placeholder="유형을 입력하세요."></Input>
    <InputTitle>보호자 정보(선택)</InputTitle>
    <RelateType>
        <RelateOption value=""></RelateOption>
    </RelateType>
    <Input relatePhone placeholder="전화번호를 입력하세요."></Input>
    <SubmitButton>
    확인
    </SubmitButton>
    </>
  );
}

export default LoginView;