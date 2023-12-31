import React from "react";

import {
  TextField,
  TextFieldProps
} from "@mui/material";
import { styled } from "@mui/system";

interface FilledInputFieldStyles {
  background? : string;
  hoverbackground? : string;
  focusedbackground? : string;
  labelColor? : string;
}

export interface FilledInputFieldProps extends Omit<TextFieldProps, 'variant'>, FilledInputFieldStyles {
  value : string;
  type? : string;
  onChange : (e :  React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => any;
}


const FilledTextField = styled(TextField)<FilledInputFieldStyles>((props) => ({
  "& .MuiFilledInput-root": {
    backgroundColor: props.background || "#fff"
  },
  "& .MuiFilledInput-root:hover": {
    backgroundColor: props.hoverbackground || "#fff",
    "@media (hover: none)": {
      backgroundColor: props.background || "#fff"
    }
  },
  "& .MuiFilledInput-root.Mui-focused": {
    backgroundColor: props.focusedbackground || "#fff"
  },
  "& .MuiFormLabel-root" : {
    color : props.labelColor || "grey"
  }
}))


export function FilledInputField(props : FilledInputFieldProps) {

  return (
    <FilledTextField
      type={props.type || "text"}
      error={props.error || false}
      required={props.required || false}
      placeholder={props.placeholder}
      label={props.label}
      fullWidth={props.fullWidth}
      value={props.value}
      onChange={props.onChange}
      multiline={props.multiline}
      size={props.size}
      variant="filled"
      background={props.background}
      hoverbackground={props.hoverbackground}
      focusedbackground={props.focusedbackground}
      labelColor={props.labelColor}
    />
  )  
}