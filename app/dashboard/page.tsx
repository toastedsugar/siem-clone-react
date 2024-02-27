import LogItemContainer from "@/components/LogItemContainer";

export default function Page() {
  return (
    <div className="flex flex-col gap-4">
      <LogItemContainer>Main Dashboard</LogItemContainer>
      <LogItemContainer>Service 1</LogItemContainer>
      <LogItemContainer>Service 2</LogItemContainer>
      <LogItemContainer>Service 3</LogItemContainer>
    </div>
  );
}
